import os

API_VERSION = '5.126'

GROUP_ID = os.environ.get('GROUP_ID')
GROUP_TOKEN = os.environ.get('GROUP_TOKEN')

APP_ID = os.environ.get('APP_ID')
ACESS_TOKEN = os.environ.get('ACESS_TOKEN')
SERVICE_TOKEN = os.environ.get('SERVICE_TOKEN')

#	resp = requests.post(f'https://oauth.vk.com/authorize?client_id={yourname}&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token&redirect_uri=https://oauth.vk.com')

waiting_for_a_post = 0
users_id_list = list()

POSTS_COUNT = 20
NEW_POSTS_COUNT = 3
