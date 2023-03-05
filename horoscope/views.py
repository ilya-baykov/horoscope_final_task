from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from horoscope.requst_prediction import *
from horoscope.support_function_views import *


# Create your views here.
def menu(request):
    """ Выводит меню всех знаком зодиака"""

    contex = {
        "all_signs_list": all_signs_list,
    }
    return render(request, "horoscope/main_menu_zodiacs.html", context=contex)


#
def current_sign_info_str(request, current_sign):
    """ Выводит информацию о конкретном знаке зодиака """

    current_sign_class = Prediction(current_sign)
    data = {
        'current_sign': current_sign,
        'validation': all_signs_dict.get(current_sign),
        "prediction": str(current_sign_class.prediction), "warning": str(current_sign_class.warning),
    }
    return render(request, 'horoscope/current_sign_info.html', context=data)


def current_sign_info_int(request, current_sign_int):
    """ Переводит на ссылку с информацией о конкретном знаке зодиака
    * срабатывает, если пользователь ввел числовое значение ( номер знака ) * """
    if len(all_signs_dict) >= current_sign_int > 0:
        url_link = reverse("current_sign_url", args=(list(all_signs_list)[current_sign_int - 1],))
        return HttpResponseRedirect(url_link)
    else:
        return HttpResponseNotFound(f"Извините, но мы не знаем знак зодиака под номером {current_sign_int}")


def type_menu(request):
    """ Выводит меню стихий знаков зодиака """
    contex = {
        "signs_types": signs_type_en_ru
    }
    return render(request, "horoscope/zodiacs_type_menu.html", context=contex)


def current_type_func(request, current_type):
    """ Выводит меню всех знаков зодиака конкретной стихии  """

    contex = {
        "current_type": current_type,
        "elem_signs": ZodiacSign.elem_signs.get(signs_type_en_ru.get(current_type))
    }
    return render(request, "horoscope/menu_elem_signs.html", context=contex)


def time_search(request, month, day):
    """ Выводит найденный по дате ( месяц , день ) знак зодиака """

    quantity = month_quantity_dict.get(month)
    info = search_sign_by_date(month, day, quantity)
    contex = {
        "sign_name_en": info[0],
        "sign_month_position": month,
        "month": MONTH_POSITION.get(month),
        "day_of_the_month": day,
        "sign_info": ZodiacSign.all_sign.get(info[0])[1]
    }
    return render(request, "horoscope/Sign_Found_by_date.html", context=contex)
