import logging

from vk.exceptions import VkAPIError
import time

from src.auth import api
from src.models import conversations, messages


def get_dialogs(offset: int = 0, batch_size: int = 200):
    """
    
    :param offset: 
    :param batch_size: 
    :return: 
    """

    while True:
        # Question: is it good practice for repeating try-except blocks?
        while True:
            try:
                response = api.messages.getDialogs(offset=offset, count=batch_size)
            except VkAPIError:
                logging.debug("Request limit")
                time.sleep(1)
                continue
            break

        offset += batch_size

        batch_size = response['count'] - offset if response['count'] - offset < batch_size else batch_size

        conversations.insert_many(response['items'])

        if offset >= response['count']:
            break


def parse_messages(conversation_id: int, offset: int = 0, batch_size: int = 200):
    while True:
        # Question: is it good practice for repeating try-except blocks?
        while True:
            try:
                response = api.messages.getHistory(user_id=conversation_id, offset=offset, count=batch_size)
            except VkAPIError:
                logging.debug("Request limit")
                time.sleep(1)
                continue
            break

        offset += batch_size

        batch_size = response['count'] - offset if response['count'] - offset < batch_size else batch_size
        messages.insert_many(response['items'])

        if offset >= response['count']:
            break


if __name__ == '__main__':
    # # For debug only: cleaning database before running
    # conversations.delete_many({})
    # messages.delete_many({})

    logging.basicConfig(level=logging.INFO)
    logging.info("Requesting of conversation list")
    get_dialogs()
    logging.info("Done! Parsed {0} conversations".format(conversations.count()))

    for conversation in conversations.find():
        info = conversation['message']
        conversation_id = int(info['chat_id']) + 2000000000 if ('chat_id' in info) else info['user_id']

        logging.info("Conversation: {0}".format(conversation_id))

        parse_messages(conversation_id)

    logging.info("Done! Parsed {0} messages".format(messages.count()))
