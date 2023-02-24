class DataTime:
    __month_info = {}

    def __init__(self, position: int, month: str, quantity: int):
        self.__position = position
        self.__month = month

        self.__quantity = quantity
        DataTime.__month_info.setdefault(position, []).extend([month, quantity])

    @classmethod
    @property
    def data_month_info(cls) -> dict:
        return cls.__month_info


DataTime(1, "январь", 31)
DataTime(2, "февраль", 28)
DataTime(3, "март", 31)
DataTime(4, "апрель", 30)
DataTime(5, "май", 31)
DataTime(6, "июнь", 30)
DataTime(7, "июль", 31)
DataTime(8, "август", 31)
DataTime(9, "сентябрь", 30)
DataTime(10, "октябрь", 31)
DataTime(11, "ноябрь", 30)
DataTime(12, "декабрь", 31)

