from django.urls import path, include
from horoscope import views as vs

urlpatterns = [
    path('menu', vs.menu),
    path('type', vs.type_menu, name="url_type"),
    path('type/<str:current_type>', vs.current_type),
    path("<int:current_sign_int>", vs.current_sign_info_int),
    path("<str:current_sign>", vs.current_sign_info_str, name="current_sign_url"),
]
