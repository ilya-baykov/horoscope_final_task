import requests
from bs4 import BeautifulSoup





class Prediction:

    def __init__(self, current_sign: str):
        self.__current_sign = current_sign
        self.url = f"https://horo.mail.ru/prediction/{self.__current_sign}/today"
        self.request_info = requests.get(self.url, auth=('user', 'pass'))

    def treatment_info(self):
        html_text = self.request_info.text
        soup = BeautifulSoup(html_text, "lxml")
        try:
            test = soup.find('div',
                             class_='article article_white article_prediction article_collapsed margin_top_20').find_all(
                "p")
            return test
        except AttributeError:
            return [False, False]

    @property
    def prediction(self):
        return list(Prediction.treatment_info(self))[0]

    @property
    def warning(self):
        return list(Prediction.treatment_info(self))[1]
