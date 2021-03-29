# Main app file

import api
import regex_handler, default_handler, publish_post, search_by_topic
#import util
import random
import config




# Responds to incoming messages
def responder(event):
	msg = event.text
	user_id = event.user_id
	message = msg+'\n'+str(user_id)

	def chous_answer():
		a=publish_post.handle(event) \
			or search_by_topic.handle(event) \
            or regex_handler.handle(msg) \
			or default_handler.handle()
		return a

	if user_id in config.users_id_list_post:
		ans = api.publish(user_id,msg)

	elif user_id in config.users_id_list_find:
		ans = api.find_story_by_topic(msg, user_id)

	else: ans = chous_answer()


	# Apply some transformations, allowing handlers to return callables and lists
	if callable(ans): ans = ans()
	if type(ans) is list: ans = random.choice(ans)
	if type(ans) is str: ans = {'message': ans}

	# Send the reply
	ans['user_id'] = event.user_id
	ans['random_id'] = random.randint(0, 2048)
	api.send(ans)


# App entrypoint
api.start()
api.poll_for_msg(responder)
