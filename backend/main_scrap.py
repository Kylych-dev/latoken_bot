from datetime import datetime, timedelta
import requests
# parsing website
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time



url = 'https://latoken.me/culture-139'
response = requests.get(url)
soup = bs(response.text, 'html.parser')



'''
id="_luF_Q"
'''

# news_headlines = soup.find_all('h2', class_='news-headline')
# for headline in news_headlines:
#     print(headline.text.strip())