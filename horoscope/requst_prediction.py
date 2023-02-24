import requests
from bs4 import BeautifulSoup


class Prediction:

    def __init__(self, current_sign: str):
        self.__current_sign = current_sign
        self.url = f"https://horo.mail.ru/prediction/{self.__current_sign}/today"

    def request_info(self):
        return requests.get(self.url, auth=('user', 'pass'))

    def treatment_info(self):
        html_text = Prediction.request_info(self).text
        soup = BeautifulSoup(html_text, "lxml")
        return soup.find('div',
                         class_='article article_white article_prediction article_collapsed margin_top_20').find_all(
            "p")

    @property
    def prediction(self):
        return list(Prediction.treatment_info(self))[0]

    @property
    def warning(self):
        return list(Prediction.treatment_info(self))[1]
