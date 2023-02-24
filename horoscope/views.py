from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from horoscope.support_cls import *
from horoscope.support_function_views import *

all_signs_dict = ZodiacSign.all_sign
all_signs_list = list(ZodiacSign.all_sign)
print(all_signs_dict)


# Create your views here.
def test(request):
    return HttpResponseNotFound(f"Данная страница еще не создана ;3")


#
def current_sign_info_str(request, current_sign):
    validation = all_signs_dict.get(current_sign)
    if validation:
        return display(current_sign, validation)
    else:
        return HttpResponseNotFound(f"Извините, но мы не знаем такой знак зодиака {current_sign}")


def current_sign_info_int(request, current_sign_int):
    if len(all_signs_dict) >= current_sign_int > 0:
        url_link = reverse("current_sign_url", args=(list(all_signs_list)[current_sign_int - 1],))
        return HttpResponseRedirect(url_link)
    else:
        return HttpResponseNotFound(f"Извините, но мы не знаем знак зодиака под номером {current_sign_int}")
