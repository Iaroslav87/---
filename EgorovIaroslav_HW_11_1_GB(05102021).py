"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:
    date: str
    def __init__(self, date):
        self.date = date

    @classmethod
    def dd1(cls, self):
        d = int(self.date[0:2])
        m = int(self.date[3:5])
        y = int(self.date[6:10])
        return Date.valid(d, m, y)

    @staticmethod
    def valid(d, m, y):
        if 0 < d < 32:
            if 0 < m < 13:
                if 0 < y < 2022:
                    return f'Day: {d}\nMonth: {m}\nYear: {y}'


d1 = Date("10-11-2021")
print(Date.dd1(d1))