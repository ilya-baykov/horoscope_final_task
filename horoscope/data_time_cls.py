from datetime import date
import calendar


class DataTime:
    __month_info = {}

    def __init__(self, month: int, quantity: int):
        self.__month = month

        self.__quantity = quantity
        DataTime.__month_info.setdefault(month, quantity)

    @classmethod
    @property
    def data_month_info(cls) -> dict:
        return cls.__month_info


current_year = date.today().year
my_calendar = calendar.Calendar()

# создаем экземпляры класса DataTime
# {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for month_position in range(1, 12 + 1):
    DataTime(month_position, max(my_calendar.itermonthdays(current_year, month_position)))
