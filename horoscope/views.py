from django.shortcuts import render
from django.http import HttpResponseNotFound


# Create your views here.
def test(requst):
    return HttpResponseNotFound(f"Данная страница еще не создана ;3")
