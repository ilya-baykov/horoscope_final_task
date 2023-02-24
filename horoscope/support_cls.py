class ZodiacSign:
    all_sign = {}
    elem_signs = {}
    intervals = {}

    def __init__(self, sign: str, description: str, element: str, time: list):
        self.__sign = sign
        self.__description = description
        self.__element = element
        self.__time = time
        ZodiacSign.all_sign.setdefault(self.__sign, [self.__sign, self.__description, self.__element, self.__time])
        ZodiacSign.elem_signs.setdefault(self.__element, []).append(self.__sign)
        ZodiacSign.intervals.setdefault(self.__sign, time)

    @classmethod
    def all_sign_info(cls):
        return cls.all_sign

    @classmethod
    def elem_signs_info(cls):
        return cls.elem_signs

    def __str__(self):
        return f"{self.__sign, self.__description, self.__element, self.__time}"


ZodiacSign("aries", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).", "Огня", [80, 110])

ZodiacSign("taurus", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).", "Земли", [111, 141])
ZodiacSign("gemini", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
           "Воздушные", [142, 172])
ZodiacSign("cancer", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).", "Водные", [173, 203])
ZodiacSign("leo", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).).", "Огня", [204, 233])
ZodiacSign("virgo", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
           "Земли", [234, 266])
ZodiacSign("libra", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
           "Воздушные", [277, 296])
ZodiacSign("scorpio", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
           "Водные", [297, 326])
ZodiacSign("sagittarius",
           "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).", "Огня", [327, 357])
ZodiacSign("capricorn", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
           "Земли", [358, 365, 1, 20])

ZodiacSign("aquarius",
           "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
           "Воздушные", [21, 50]),
ZodiacSign("pisces", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
           "Водные", [51, 79])
