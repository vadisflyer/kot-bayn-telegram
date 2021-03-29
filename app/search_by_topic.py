import config

def handle(event):
	msg = event.text
	buf = find_post.get(msg.lower())
	if buf:
		config.users_id_list_find.append(event.user_id)
		return buf

# Matches the key exactly, ignoring the case
find_post = {
    'найди': 'Скажите, на какую тему мне найти сказку?\nЛибо для отмены скажите: [Стоп]'
}
