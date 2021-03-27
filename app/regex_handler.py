import api
import util

# Matches regular expressions (regexes), ignoring the case
def handle(msg):
	for regex, ans in regexTable.items():
		if regex.search(msg): return ans
h_answer = 'Я рассказываю сказки, на ночь, на день, на свадбе. Вы можете воспользоваться следующими командами (все лишние слова могут помешать нашему общению).\n\n[Сказку] - я расскажу вам одну из своих сказок, на свой выбор.\n[Новую сказку] - расскажу самую последнюю, свежую сказку.\n[Найди] - найду сказку по ключевому слову или словам. Очень рекомендую.\n[Запиши] - могу запомнить вашу и рассказывать её другим. \n\nТолько введите команду.'

regexTable = {
    r'привет': 'Здравствуй :)\n' + h_answer,
    r'как дела': [
		'Дождик льёт, да не на меня!)',
		'Солнышко светит!)',
	],
	r'новую сказку': api.sendNewStory,
	r'сказку': api.sendStory,
    r'помощь|команды|help|-h|^\?$': h_answer
}

# Compile the regexes in the keys
regexTable = {util.compileRegex(pattern): ans for pattern, ans in regexTable.items()}
