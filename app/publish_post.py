
import config

def handle(event):
	msg = event.text
	buf = verbatim_post_specific.get(msg.lower())
	if buf:
		config.users_id_list.append(event.user_id)
		return buf

# Matches the key exactly, ignoring the case
verbatim_post_specific = {
    'запиши': 'Ожидаю. Следующее ваше сообщение будет опубликовано! \nДля отмены скажите: [стоп]'
}
