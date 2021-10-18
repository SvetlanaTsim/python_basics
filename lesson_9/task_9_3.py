"""
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры
класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage,'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

secretary = Position('Marina','Ivanova','secretary', 30, 20)
print(secretary.get_full_name())
print(secretary.get_total_income())

director = Position('Petr','Stepanov', 'CEO', 50, 30)
print(director.get_full_name())
print(director.get_total_income())

