from django.http import HttpResponseNotFound, HttpResponse


def display(current_sign, info: list):
    res = f"<h1><div style='text-align: center;'>{info[0]}</div></h1><br>"
    res += f"<h2>{info[1]}</h2>"
    res += f"<p>Советы на сегодня</p>"
    res += ""
    return HttpResponse(f"{res}")
