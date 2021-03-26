from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType

import config
import util
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
def poll(callback):
	#try:
	events = VkLongPoll(vk_group)
	for event in events.listen():
		if event.type is VkEventType.MESSAGE_NEW and event.to_me:
			callback(event)
	#except BaseException as e: print(e)

def send(options):
    vk_group.method('messages.send', options)
    

# Sends a random story from `count` most recent stories on the wall
def sendStory(count = config.POSTS_COUNT):
	response = vk_service.method('wall.get', {
		'owner_id': config.GROUP_ID,
		'count': count
	})
	count = min(count, response['count'])
	story = util.selectRandom(response['items'], count - 1)
	#print(story)
	return {'attachment': 'wall' + config.GROUP_ID + '_' + str(story['id'])}

def sendNewStory():
	return sendStory(config.NEW_POSTS_COUNT)

def publish(user_id,msg):
	if msg not in ['стоп', 'Стоп', 'Отмена', 'отмена']:
		user = vk_acess_wall_post.method("users.get", {"user_ids": user_id}) 
		fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']

		message = msg + '\nАвтор : *id'+str(user_id)+' ('+fullname+')'
		post_msg={
			r'owner_id': config.GROUP_ID,
			r'from_group': 1,
			r'message': message,
			r'guid' : random.randint(0, 2048),
			r'signed': 0,
			r'v':config.API_VERSION

		}

		vk_acess_wall_post.method('wall.post', post_msg)
		ans =  'Спасибо, что вы с нами. Пишите еще!)'
	else: ans =  'Галя, у нас отмена!'
	return ans
