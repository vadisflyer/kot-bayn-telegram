import requests
from bs4 import BeautifulSoup
import random
import re
import json

data = {
    "THE BIRTH OF THE FAIRY TALE": {
        "LANGUAGE": None,
        "AUTHOR": None,
        "PAGE": 1
    },
    "SNOW-WHITE AND ROSY-RED": {
        "LANGUAGE": "Danish",
        "AUTHOR": "TORGEN MOE AND P. ASBIÖRNSON",
        "PAGE": 9
    },
    "THE STORY OF ARGILIUS AND THE FLAME KING": {
        "LANGUAGE": "Slavonic",
        "AUTHOR": "COUNT MAYLÁTH",
        "PAGE": 20
    },
    "PERSEVERE AND PROSPER": {
        "LANGUAGE": "Arabic",
        "AUTHOR": "DR. G. WEIL",
        "PAGE": 38
    },
    "PRINCE OF THE GLOW-WORMS": {
        "LANGUAGE": "German",
        "AUTHOR": "FRIEDRICH VON SALLET",
        "PAGE": 41
    },
    "THE TWO MISERS": {
        "LANGUAGE": "Hebrew",
        "AUTHOR": None,
        "PAGE": 71
    },
    "PRINCE CHAFFINCH": {
        "LANGUAGE": "French",
        "AUTHOR": None,
        "PAGE": 73
    },
    "THE WOLF AND THE NIGHTINGALE": {
        "LANGUAGE": "Swedish",
        "AUTHOR": "E. M. ANNDT",
        "PAGE": 105
    },
    "THE ENCHANTED CROW": {
        "LANGUAGE": "Polish",
        "AUTHOR": "K. W. WOYCICKY",
        "PAGE": 132
    },
    "THE DRAGON-GIANT AND HIS STONE STEED": {
        "LANGUAGE": "Russian",
        "AUTHOR": "O. L. B. WOLFF",
        "PAGE": 153
    },
    "THE STORY OF SIVA AND MADHAVA": {
        "LANGUAGE": "Sanskrit",
        "AUTHOR": "SOMADEVA BHATTA",
        "PAGE": 185
    },
    "THE GOBLIN BIRD": {
        "LANGUAGE": "Betschuanian",
        "AUTHOR": "CASALIS",
        "PAGE": 201
    },
    "THE SHEPHERD AND THE SERPENT": {
        "LANGUAGE": "German",
        "AUTHOR": None,
        "PAGE": 209
    },
    "THE EXPEDITIOUS FROG": {
        "LANGUAGE": "Wendian",
        "AUTHOR": "LEOPOLD HAUSST AND J. E. SCHMALER",
        "PAGE": 215
    },
    "EASTWARD OF THE SUN, AND WESTWARD OF THE MOON": {
        "LANGUAGE": "Norwegian",
        "AUTHOR": "P. ASBIÖRNSON",
        "PAGE": 217
    },
    "THE LITTLE MAN IN GREY": {
        "LANGUAGE": "Upper Lusatian",
        "AUTHOR": "MONTZ HAUSST",
        "PAGE": 236
    },
    "RED, WHITE, AND BLACK": {
        "LANGUAGE": "Norman",
        "AUTHOR": "L'HERITIER",
        "PAGE": 243
    },
    "THE TWELVE LOST PRINCESSES AND THE WIZARD KING": {
        "LANGUAGE": "African",
        "AUTHOR": None,
        "PAGE": 249
    },
    "THE STUDY OF MAGIC UNDER DIFFICULTIES": {
        "LANGUAGE": "Italian",
        "AUTHOR": "STRAPPAROLA",
        "PAGE": 268
    },
    "FORTUNE'S FAVOURITE": {
        "LANGUAGE": "Hungarian",
        "AUTHOR": "G. VON GALL",
        "PAGE": 281
    },
    "THE LUCKY DAYS": {
        "LANGUAGE": "Italian",
        "AUTHOR": "STRAPPAROLA",
        "PAGE": 309
    },
    "THE FEAST OF THE DWARFS": {
        "LANGUAGE": "Icelandish",
        "AUTHOR": None,
        "PAGE": 313
    },
    "THE THREE DOGS": {
        "LANGUAGE": "Frieslandish",
        "AUTHOR": "L. BECKSTEIN",
        "PAGE": 329
    },
    "THE COURAGEOUS FLUTE-PLAYER": {
        "LANGUAGE": "Franconian",
        "AUTHOR": None,
        "PAGE": 339
    },
    "THE GLASS HATCHET": {
        "LANGUAGE": "Hungarian",
        "AUTHOR": "G. VON GALL",
        "PAGE": 345
    },
    "THE GOLDEN DUCK": {
        "LANGUAGE": "Bohemian",
        "AUTHOR": "WOLFGARD A. GERLE",
        "PAGE": 360
    },
    "GOLDY": {
        "LANGUAGE": "German",
        "AUTHOR": "JUSTINUS KERNER",
        "PAGE": 377
    },
    "THE SERPENT PRINCE": {
        "LANGUAGE": "Italian",
        "AUTHOR": "BASILE",
        "PAGE": 384
    },
    "THE PROPHETIC DREAM": {
        "LANGUAGE": None,
        "AUTHOR": None,
        "PAGE": 398
    }
}

# Функция для поиска разделителя с учетом регистра
def find_case_sensitive_delimiter(text, delimiter):
    index = text.find(delimiter)
    if index != -1:
        if text[index:index+len(delimiter)] == delimiter:
            return index
    return -1

# Функция для получения случайной книги с Project Gutenberg и ее текста
def get_random_gutenberg_book():
    url = "https://www.gutenberg.org/ebooks/search/?sort_order=random"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
#        print(f"{soup=}")
        link = soup.find_all('li', class_='booklink')[0]
        print(f"{link.prettify()}")
        href = link.find('a', class_='link').get('href')
#        print(f"{href=}")
        
        title = link.find('span', class_='title').text
#        print(f"{title}")
        subtitle = link.find('span', class_='subtitle').text
#        print(f"{subtitle}")
#        print(f"href={href}")
#        if links:
#            random_link = random.choice(links)
#            return [random_link]
#get_random_gutenberg_book()
def get_book_content(url):
    response = requests.get(url)
    if response.status_code == 200:
#        print(response.text)
#        start_index = response.text.find('CONTENTS.')

#        if start_index != -1:
        # Вырезаем текст после целевой строки
#                result_text = response.text[start_index:]
#                print(result_text)
#        else:
#                print("Целевая строка не найдена в тексте.")
        start_of_contents = 'fond recollection on the golden birth of those Fairy charms.'
        end_of_contents = '[Illustration: THE PROPHETIC DREAM. P. 406.]'
        content_text = response.text.partition(end_of_contents)[0].rpartition(start_of_contents)[2]
        # Регулярное выражение для поиска строк с иллюстрациями
        pattern = r'\[Illustration(?:[^\]]+)?\]'
        content_text = re.sub(pattern, '', content_text)
#        content_list = re.sub(r'(\s+)(?!\s)', ':', content_text)
#        print(content_text)
# Получите список названий сказок из JSON
        tales = list(data.keys())
        for tale in reversed(tales):
#                print(tale)
                # Ищем разделитель "AND" с учетом регистра
            delimiter = f"{tale}.\r\n"
#                delimiter_index = find_case_sensitive_delimiter(content_text, delimiter)
            content_text, _, data[tale]["STORY"] = content_text.partition(delimiter)

#                if delimiter_index != -1:
#                    before, _, after = original_string.partition(original_string[delimiter_index:delimiter_index+len(delimiter)])
#                    print("Before:", before)
#                    print("Delimiter:", delimiter)
#                    print("After:", after)
#                else:
#                    print(f"Delimiter '{delimiter}' not found.")
#                content_text, _, data[tale]["STORY"] = content_text.rpartition(content_text[delimiter_index:delimiter_index+len(content_text)])
                #data[tale]["STORY"] = parts[2]
                #content_text = parts[0]
# Выберите случайную сказку из списка
        random_tale = random.choice(tales)

# Получите информацию о выбранной сказке
        selected_tale = data[random_tale]
        print(selected_tale)
        output = f"Название сказки: {random_tale}\nАвтор: {selected_tale['AUTHOR']}\nСказка: {selected_tale['STORY']}"
#        print(output)
#        print("Название сказки:", random_tale)
#        print("Автор:", selected_tale["AUTHOR"])
#        print("Сказка:", selected_tale["STORY"])
        return output