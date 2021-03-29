import api
import re

# Matches regular expressions (regexes), ignoring the case
def handle(msg):
	for regex, ans in regex_table.items():
		if regex.search(msg): return ans
h_answer = '''
            Я рассказываю сказки, на ночь, на день, на свадбе. Вы можете воспользоваться следующими командами (все лишние слова могут помешать нашему общению).
            
            [Сказку] - я расскажу вам одну из своих сказок, на свой выбор.
            [Новую сказку] - расскажу самую последнюю, свежую сказку.
            [Найди] - найду сказку по ключевому слову или словам. Очень рекомендую.
            [Запиши] - могу запомнить вашу и рассказывать её другим. 
            
            Только введите нужную команду.'''

regex_table = {
    r'привет': 'Здравствуй :)' + h_answer,
    r'как дела': [
		'Дождик льёт, да не на меня!)',
		'Солнышко светит!)',
	],
	r'новую сказку': api.send_new_story,
	r'сказку': api.send_story,
    r'помощь|команды|help|-h|^\?$': h_answer
}

regex_table = {re.compile(pattern, re.IGNORECASE): ans for pattern, ans in regex_table.items()}

