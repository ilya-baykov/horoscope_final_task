from django.http import HttpResponse
from django.urls import reverse
from horoscope.requst_prediction import Prediction
from horoscope.support_cls import ZodiacSign
from horoscope.data_time_cls import DataTime
import re

all_signs_dict = ZodiacSign.all_sign
all_signs_list = list(ZodiacSign.all_sign)
signs_type = {
    "fire": "Огня",
    "earth": "Земли",
    "air": "Воздушные",
    "water": "Водные"
}


def display_elem_sign(current_type):
    total_display = "<ul>"
    elem_signs = ZodiacSign.elem_signs.get(current_type)
    for sign in elem_signs:
        url_link = reverse("current_sign_url", args=(sign,))
        total_display += f"<li><a href = '{url_link}'>{sign}</a></li>"
    total_display += "</ul>"
    return HttpResponse(f"{total_display}")


def display_date_search(sign, month, day):
    """ Выводит на экран ссылку на нужный знак зодиака"""
    url_link = reverse("current_sign_url", args=(sign,))
    month_info = DataTime.data_month_info.get(month)
    total_display = f"<h2>Месяц - {month_info[0]} ,<br> день - {day}</h2>"
    sign_info = ZodiacSign.all_sign.get(sign)
    total_display += f"<a href = '{url_link}'>{sign_info[1]}</a>"
    return HttpResponse(f"{total_display}")


def time_search_sign(month, day):
    """Определяет какой знак зодиака нужно вывести на экран"""
    day_of_the_year_result = day_of_the_year(month) + day
    intervals = ZodiacSign.intervals
    for sign, interval in intervals.items():
        verdict = interval[0] <= day_of_the_year_result <= interval[1]
        if verdict:
            return display_date_search(sign, month, day)
    return display_date_search("capricorn", month, day)


def day_of_the_year(month) -> int:
    """ Суммирует количество дней предыдуших месяцев """
    result = 0
    current_month = 1
    while current_month < month:
        result += DataTime.data_month_info.get(current_month)[1]
        current_month += 1
    return result
