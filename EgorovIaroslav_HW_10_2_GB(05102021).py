"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class WorkingForm(ABC):
    @abstractmethod
    def fabric_calculation(self):
        pass


class Coat(WorkingForm):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_calculation(self):
        V = self.v / 6.5 + 0.5
        return f'Ткани понадобится на пальто: {V}'


class Suite(WorkingForm):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_calculation(self):
        H = 2 * self.h + 0.3
        return f'Ткани понадобится на костюм: {H}'


class TotalFabric(WorkingForm):
    def __init__(self, v, h):
        self.V = v
        self.H = h

    @property
    def fabric_calculation(self):
        all = (self.V / 6.5 + 0.5) + (2 * self.H + 0.3)
        return f'Всего ткани понадобится: {all}'


coat = Coat(50)
suite = Suite(189)
total = TotalFabric(50, 189)
print(suite.fabric_calculation)
print(coat.fabric_calculation)
print(total.fabric_calculation)