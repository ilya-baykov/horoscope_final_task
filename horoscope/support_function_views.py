from django.http import HttpResponse
from django.urls import reverse
from horoscope.requst_prediction import Prediction
from horoscope.support_cls import ZodiacSign

all_signs_dict = ZodiacSign.all_sign
all_signs_list = list(ZodiacSign.all_sign)
signs_type = {
    "fire": "Огня",
    "earth": "Земли",
    "air": "Воздушные",
    "water": "Водные"
}


def display(current_sign, info: list):
    current_sign = Prediction(current_sign)
    res = f"<h1><div style='text-align: center;'>{info[1]}</div></h1><br>"
    res += f"<p><b>Советы на сегодня</b></p>"
    res += f"{current_sign.prediction}"
    res += f"<p><b>Будьте осторожней</b></p>"
    res += f"{current_sign.warning}"
    return HttpResponse(f"{res}")


def display_menu():
    total = f"<h3><div style='text-align: center;'>Меню выбора знака зодиака</div></h3>"
    total += "<ol>"
    for sign in all_signs_list:
        url_link = reverse("current_sign_url", args=(sign,))
        total += f"<li><a href = '{url_link}'>{sign.title()}</a></li>"
    total += "</ol>"
    return HttpResponse(f"{total}")


def display_type_menu():
    total_display = f"<h3><div style='text-align: center;'>Стихии знаков зодиака</div></h3>"
    total_display += "<ul>"
    for elem in signs_type:
        url_link = reverse("url_type")
        total_display += f"<li><a href = '{url_link}/{elem}'>{elem}</a></li>"
    total_display += "</ul>"
    return HttpResponse(f"{total_display}")
