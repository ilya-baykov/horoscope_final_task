from horoscope.support_cls import ZodiacSign
from horoscope.data_time_cls import DataTime

all_signs_dict = ZodiacSign.all_sign
all_signs_list = list(ZodiacSign.all_sign)

signs_type_en_ru = {
    "fire": "Огня",
    "earth": "Земли",
    "air": "Воздушные",
    "water": "Водные"
}

MONTH_POSITION = dict(zip(
    [int(i) for i in range(1, 13)],
    ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
     "Декабрь"]))

month_quantity_dict = DataTime.data_month_info


def search_sign_by_date(month: int, day: int, quantity: int) -> str | tuple:
    """ Проверяет коректность переданных параметров и вызывает вспомогательные функции """
    if 12 >= month > 0 and quantity >= day > 0:
        return time_search_sign(month, day)
    else:
        return f"Дата введена неверно - {day} {month}"


def time_search_sign(month: int, day: int) -> tuple:
    """Определяет какой знак зодиака нужно вывести на экран"""
    day_of_the_year_result = day_of_the_year(month) + day
    intervals = ZodiacSign.intervals
    for sign, interval in intervals.items():
        verdict = interval[0] <= day_of_the_year_result <= interval[1]
        if verdict:
            return sign, month, day
    return "capricorn", month, day


def day_of_the_year(month: int) -> int:
    """ Суммирует количество дней предыдуших месяцев """
    result = 0
    current_month = 1
    while current_month < month:
        result += month_quantity_dict.get(current_month)
        current_month += 1
    return result
