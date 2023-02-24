from django.urls import path, include
from horoscope import views as vs

urlpatterns = [
    path('menu', vs.test),
]
