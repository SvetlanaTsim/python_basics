"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):
#__init__ не стала делать, так как общих атрибутов вроде нет,
# у каждого наследника будут свои.
    @abstractmethod
    def material_usage(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.size = v

    @property
    def material_usage(self):
        return round((self.size/6.5 + 0.5), 2)

class Costume(Clothes):
    def __init__(self, h):
        self.height = h

    @property
    def material_usage(self):
        return round((2*self.height + 0.3), 2)

coat_1 = Coat(5)
print(coat_1.material_usage)
costume_1 = Costume(6)
print(costume_1.material_usage)
print(f'общий расход ткани: {coat_1.material_usage+costume_1.material_usage}')



