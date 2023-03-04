from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from horoscope.data_time_cls import DataTime
from horoscope.support_function_views import *


# Create your views here.
def menu(request):
    contex = {
        "all_signs_list": all_signs_list,
    }
    return render(request, "horoscope/main_menu_zodiacs.html", context=contex)


#
def current_sign_info_str(request, current_sign):
    validation = all_signs_dict.get(current_sign)
    current_sign = Prediction(current_sign)
    data = {
        'current_sign': current_sign,
        'validation': validation,
        "prediction": str(current_sign.prediction),
        "warning": str(current_sign.warning),
    }
    return render(request, 'horoscope/current_sign_info.html', context=data)


def current_sign_info_int(request, current_sign_int):
    if len(all_signs_dict) >= current_sign_int > 0:
        url_link = reverse("current_sign_url", args=(list(all_signs_list)[current_sign_int - 1],))
        return HttpResponseRedirect(url_link)
    else:
        return HttpResponseNotFound(f"Извините, но мы не знаем знак зодиака под номером {current_sign_int}")


def type_menu(request):
    contex = {
        "signs_types": signs_type
    }
    return render(request, "horoscope/zodiacs_type_menu.html", context=contex)


def current_type(request, current_type):
    for current_type_en, current_type_ru in signs_type.items():
        if current_type == current_type_en:
            return display_elem_sign(current_type_ru)


def time_search(request, month, day):
    quantity = DataTime.data_month_info.get(month)
    if 12 >= month > 0 and quantity[1] >= day > 0:
        return time_search_sign(month, day)
    else:
        return HttpResponseNotFound(f"Вы непраильно ввели дату , {quantity[0]} {quantity[1]} дней")
