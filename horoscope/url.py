from django.urls import path, include
from horoscope import views as vs

urlpatterns = [
    path('menu', vs.test),
    path("<str:current_sign>", vs.current_sign_info_str),
]
