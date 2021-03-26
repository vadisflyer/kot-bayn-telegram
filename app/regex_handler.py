import api
import util

# Matches regular expressions (regexes), ignoring the case
def handle(msg):
	for regex, ans in regexTable.items():
		if regex.search(msg): return ans
h_answer = 'Я рассказываю сказки, на ночь, на день, на свадбе. команда:[Сказку\\Новую сказку]. Очень рекомендую, эта команда тут самая ключевая.\n Могу запомнить твою и рассказывать её другим. Только введи: [Запиши]'

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
