import api
import util

# Matches regular expressions (regexes), ignoring the case
def handle(msg):
	for regex, ans in regexTable.items():
		if regex.search(msg): return ans

regexTable = {
	r'доброе утро': 'И тебе солнечного)',
	r'спок': 'Добрых снов)',
    r'привет': 'Здравствуй :)\nЯ рассказываю сказки, на ночь, на день, на свадбе. команда:[Сказку\\Новую сказку]. Очень рекомендую, эта команда тут самая ключевая.\n Могу запомнить твою и рассказывать её другим. Только введи: [Запиши]\n Также могу оказать [Помощь]',
    r'как дела': [
		'Дождик льёт, да не на меня! Как твои?)',
		'Солнышко светит! Как твои?)'
	],
	r'пока': 'до новых встреч ^_^',
	r'новую сказку': api.sendNewStory,
	r'сказку': api.sendStory,
    r'как писать?|помощь|команды|help|-h|^\?$': 'Я люблю, когда говорят прямо!\nХочешь сказку - пиши "Сказку".\nPS хотя и поболтать тоооже можноо)\n&#128521;'
}

# Compile the regexes in the keys
regexTable = {util.compileRegex(pattern): ans for pattern, ans in regexTable.items()}
