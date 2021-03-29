from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

import config
import random


# Logins with two different tokens
def start():
	global vk_group, vk_service, vk_acess_wall_post

	# API for sending and recieving messages
	vk_group = VkApi(token = config.GROUP_TOKEN)
	# API for reading the wall
	vk_service = VkApi(token = config.SERVICE_TOKEN)

	vk_acess_wall_post = VkApi(token = config.ACESS_TOKEN)
	

# Calls `callback` for each new message
def poll_for_msg(callback):
	#try:
	events = VkLongPoll(vk_group)
	for event in events.listen():
		if event.type is VkEventType.MESSAGE_NEW and event.to_me:
			callback(event)
	#except BaseException as e: print(e)

def send(options):
    vk_group.method('messages.send', options)
    

# Sends a random story from `count` most recent stories on the wall
def send_story(count = config.POSTS_COUNT):
	response = vk_service.method('wall.get', {
		'owner_id': config.GROUP_ID,
		'count': count
	})
	count = min(count, response['count'])
	story = random.choice(response['items'][:count])
	return {'attachment': 'wall' + config.GROUP_ID + '_' + str(story['id'])}

def send_new_story():
	return send_story(config.NEW_POSTS_COUNT)

def publish(user_id,msg):
	kot = '''　　　　　／＞　 フ
			　　　　　| 　_　 _|
			　 　　　／`ミ _x 彡
			　　 　 /　　　 　 |
			　　　 /　 ヽ　　 ﾉ
			　／￣|　　 |　|　|
			　| (￣ヽ＿_ヽ_)_)
			　＼二つ
		'''
	ans = verb(msg)
	if not ans:
		user = vk_acess_wall_post.method("users.get", {"user_ids": user_id}) 
		fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']

		message = f'{kot}\n{msg}\n\nАвтор : *id{str(user_id)} ({fullname})'
		post_msg={
			'owner_id': config.GROUP_ID,
			'from_group': 1,
			'message': message,
			'guid' : random.randint(0, 2048),
			'signed': 0,
			'v':config.API_VERSION
		}

		vk_acess_wall_post.method('wall.post', post_msg)
		ans =  'Спасибо, что вы с нами. Пишите еще!)'
	config.users_id_list_post.remove(user_id)
	return ans

def find_story_by_topic(msg = '',user_id = 0,count = config.POSTS_COUNT):
	ans = verb(msg)
	if (ans):
		config.users_id_list_find.remove(user_id)
	else:    
		response = vk_service.method('wall.search', {
			'owner_id': config.GROUP_ID,
			'query': msg,
			'count': count
		})
		if response['count']:
			count = min(count, response['count'])
			story = random.choice(response['items'][:count])
			story_id = str(story['id'])
			ans = {"attachment": f'wall{config.GROUP_ID}_{story_id}'}
			config.users_id_list_find.remove(user_id)
		else: ans = 'У меня нет таких сказок.(\n Предложите другую тему или для отмены скажите:"Стоп".'

	return ans

def verb(msg):
    if msg.lower() in ['стоп','отмена']:
        return 'Галя, у нас отмена!'
