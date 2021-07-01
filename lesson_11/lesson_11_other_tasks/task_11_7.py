"""
Реализовать проект «Операции с комплексными числами».
Создать класс «Комплексное число».
Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
"""
# как я поняла, комплексные числа уже в питоне реализованы, поэтому перегрузку сделала без формулы
a = 5+2j
b = 8+6j
print(a+b)
print(a*b)

class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number

a = ComplexNumber(5+2j)
b = ComplexNumber(8+6j)
print(a+b)
print(a*b)

# попробовала с формулой
class ComplexNumber2:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return f'{self.real + other.real}+{self.imag + other.imag}'

    def __mul__(self, other):
        # z1=a+bi и z2=c+di z1z2 = (ac-bd)+i(ad+cb).
        #почему-то self.imag * other.imag дают отрицательное число, изменила им знак на '+'
        return (self.real * other.real + self.imag * other.imag) + (self.imag * other.real + other.imag * self.real)

a_1 = ComplexNumber2(5, 2j)
b_1 = ComplexNumber2(8, 6j)
print(a_1+b_1)
print(a_1 * b_1)
