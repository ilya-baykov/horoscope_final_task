from django.http import  HttpResponse
from horoscope.requst_prediction import Prediction


def display(current_sign, info: list):
    current_sign = Prediction(current_sign)
    res = f"<h1><div style='text-align: center;'>{info[1]}</div></h1><br>"
    res += f"<p><b>Советы на сегодня</b></p>"
    res += f"{current_sign.prediction}"
    res += f"<p><b>Будьте осторожней</b></p>"
    res += f"{current_sign.warning}"
    return HttpResponse(f"{res}")
