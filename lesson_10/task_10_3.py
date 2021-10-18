"""
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
 В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
 вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
 Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только
если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества
 ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(),
 принимающий экземпляр класса и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
 то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

"""
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity <= 0:
            return 'Результат вычитания меньше или равен нулю'
        else:
            return self.quantity - other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __floordiv__(self, other):
        try:
            self.quantity // other.quantity
        except ZeroDivisionError:
            return 'Деление на ноль'
        else:
            return self.quantity // other.quantity

    def __truediv__(self, other):
        try:
            self.quantity // other.quantity
        except ZeroDivisionError:
            print('Деление на ноль')
        else:
            return self.quantity // other.quantity

    def make_order(self, quan_in_row):
        rows = self.quantity // quan_in_row
        rest = self.quantity % quan_in_row
        out_str = ('*' * quan_in_row + '\n') * rows + '*' * rest
        return out_str

cell_1 = Cell(5)
cell_2 = Cell(10)
cell_3 = Cell(0)

print (cell_1 + cell_2)
print (cell_1 - cell_2)
print (cell_2 - cell_1)
print (cell_2 * cell_1)
print (cell_2 // cell_1)
print (cell_1 // cell_2)
print (cell_3 - cell_1)
print (cell_1 // cell_3)
print (cell_3 / cell_1)
print(cell_2.make_order(4))
print(cell_2.make_order(1))
