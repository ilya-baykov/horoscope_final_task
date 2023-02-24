import requests
from bs4 import BeautifulSoup

URL = 'https://horo.mail.ru/prediction/aries/today'

page = requests.get(URL, auth=('user', 'pass'))

soup = BeautifulSoup(page.text, "lxml")

prediction = soup.find('div',
                       class_='article article_white article_prediction article_collapsed margin_top_20').find_all(
    "p")
prediction = list(prediction)
advice, warning = prediction

