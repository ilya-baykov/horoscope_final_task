from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from horoscope.support_cls import *
from horoscope.requst_prediction import advice, warning
from horoscope.support_function_views import *

all_signs_dict = ZodiacSign.all_sign
print(all_signs_dict)


# Create your views here.
def test(request):
    return HttpResponseNotFound(f"Данная страница еще не создана ;3")


#
def current_sign_info_str(request, current_sign):
    validation = all_signs_dict.get(current_sign)
    if validation:
        return display(current_sign, validation)
