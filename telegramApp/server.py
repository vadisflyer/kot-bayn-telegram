import telebot
import keyring as kr 

import requests
from bs4 import BeautifulSoup
import random
import get_nation_story

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = kr.get_password("AlphonsesBar", #serviceName 
                "Alphonse")  	        #username

# Замените 'YOUR_GROUP_CHAT_ID' на идентификатор вашей публичной группы
GROUP_CHAT_ID = -1001323950655  # Пример

# Инициализируем бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
#@bot.message_handler(commands=['start'])
#def handle_start(message):
#    bot.send_message(message.chat.id, 'Привет! Я эхобот. Просто отправь мне сообщение, и я повторю его.')

# Обработчик всех входящих текстовых сообщений
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)
    group_chat_id = GROUP_CHAT_ID
    text_to_post = "Пример поста для публикации в группе."
#    bot.send_message(group_chat_id, text_to_post + '\n' + message.text)
    gutenberg_book = get_random_gutenberg_book()
#    bot.send_message(message.chat.id, gutenberg_book, parse_mode='Markdown')
    send_message_in_parts(group_chat_id, gutenberg_book )

# Функция для получения случайной книги с Project Gutenberg и ее текста
def get_random_gutenberg_book():
    story = str(get_nation_story.get_book_content('https://www.gutenberg.org/files/34956/34956-8.txt'))
#    print(story)
    return story

def send_message_in_parts(chat_id, message, max_length=4096):

#if len(message) > 4096:
#        for x in range(0, len(message), max_length):
#            print(f"{message[x:x+max_length]=}")
#            bot.send_message(chat_id, message[x:x+max_length], parse_mode='Markdown')
#    else:
#        print(f"{message=}")
#        bot.send_message(chat_id, message, parse_mode='Markdown')
    if len(str(message)) <= max_length:
        bot.send_message(chat_id, message,parse_mode='Markdown')
    else:
# Разделяем строку на строки
        lines = message.splitlines()
# Берем первые три строки
        first_three_lines = lines[:3]
# Преобразуем их обратно в строку
        head = "\n".join(first_three_lines)
        part = message[:max_length]
        bot.send_message(chat_id, part)
        remaining_message = head+'\n\n' + message[max_length:]
        send_message_in_parts(chat_id, remaining_message, max_length)

# Запуск бота
bot.polling(True)