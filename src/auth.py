import json
import vk

from settings import TOKEN_FILE

with open(TOKEN_FILE) as data_file:
    data = json.load(data_file)

access_token = data['token']

vk_session = vk.Session(access_token=access_token)
api = vk.API(vk_session, v='5.64', timeout=10)
