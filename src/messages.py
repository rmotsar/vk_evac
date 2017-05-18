from src.auth import api
from src.database import session
from src.models import Conversation, Message


def get_dialogs():
    """
    
    Method for parsing all identifiers for chats and personal conversations 
    
    :return: dict() of pairs <id>:<conversation_type>
    
    """
    offset = 0
    batch_size = 200

    results = dict()

    while True:
        response = api.messages.getDialogs(offset=offset, count=batch_size)

        if (response['count'] - (offset * batch_size)) <= 0:
            break
        offset += 1

        for item in response['items']:
            conversation = Conversation()
            message = item['message']
            if 'chat_id' in message.keys():
                conversation_id = 2000000000 + int(message['chat_id'])
                conversation_type = 'chat'

            else:
                conversation_id = message['user_id']
                conversation_type = 'private'

            conversation.id = conversation_id
            conversation.type = conversation_type

            session.add(conversation)

        # todo: exception catcher
        session.commit()


def parse_messages(conversation_id: int):
    offset = 0
    batch_size = 200

    while True:
        response = api.messages.getHistory(user_id=conversation_id, offset=offset, count=batch_size)

        if (response['count'] - (offset * batch_size)) <= 0:
            break
        offset += 1

        for item in response['items']:
            message = Message(**item)

            session.add(message)
            print(item)
        session.commit()
        print(response)


def download_attachment():
    pass


if __name__ == '__main__':
    # print(get_dialogs())
    parse_messages(204816945)
