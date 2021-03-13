# Main app file

import api
import verbatim_handler, regex_handler, default_handler, publish_post
import util
import random
import config




# Responds to incoming messages
def responder(event):
	msg = event.text
	user_id = event.user_id
	message = msg+'\n'+str(user_id)

	def chous_ansver():
		a=publish_post.handle(event) \
			or verbatim_handler.handle(msg) \
			or regex_handler.handle(msg) \
			or default_handler.handle()
		return a

	if len(config.users_id_list):
		if user_id in config.users_id_list:
			config.users_id_list.remove(user_id)

			ans = api.publish(user_id,msg)
		
		else: ans = chous_ansver()
	# Try various handlers until the reply is found
	else:
		ans = chous_ansver()

	# Apply some transformations, allowing handlers to return callables and lists
	if callable(ans): ans = ans()
	if type(ans) is list: ans = util.selectRandom(ans)
	if type(ans) is str: ans = {'message': ans}

	# Send the reply
	ans['user_id'] = event.user_id
	ans['random_id'] = random.randint(0, 2048)
	api.send(ans)


# App entrypoint
api.start()
api.poll(responder)
