from datetime import datetime, timedelta
import requests
# parsing website
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time, requests





url = 'https://latoken.me/culture-139'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

# Извлекаем текстовое содержимое из элементов с классом 'kr-span'
page_content = ''
for span_tag in soup.find_all('span', class_='kr-span'):
    page_content += span_tag.get_text(strip=True) + '\n'

# Записываем содержимое в файл
filename = 'parsed_content.txt'
with open(filename, 'w', encoding='utf-8') as file:
    file.write(page_content)

print(f'Содержимое успешно сохранено в файл {filename}')


# _________________________
# url = 'https://latoken.me/culture-139'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
#
# print(soup.prettify())
# _________________________


# page_content = soup.get_text()
#
# filename = 'parsed_content.html'
#
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(page_content)
#
#
#
# print(f'Содержимое успешно сохранено в файл {filename}')



'''
id="_luF_Q"
'''

# news_headlines = soup.find_all('h2', class_='news-headline')
# for headline in news_headlines:
#     print(headline.text.strip())



