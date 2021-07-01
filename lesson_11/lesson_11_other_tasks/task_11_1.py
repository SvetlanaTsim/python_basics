"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый — с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
"""

# class Date:
#     def __init__(self):
#         date = '01.07.2021'
#             #x = '2.2'
#
#     @classmethod
#     def date_to_number(cls):
#         day, month, year = cls.date.split('.')
#         return int(day), int(month), int(year)
#
# #a = Date('01.07.2021')
# print(Date.date_to_number())
# #print(a.date)
#

class Date:
    date = '01.07.2021'

    def __init__(self, new_date):
        Date.date = new_date

    @classmethod
    def date_to_number(cls):
        day, month, year = cls.date.split('.')
        return int(day), int(month), int(year)

    @staticmethod
    def date_valid():
        day, month, year = Date.date_to_number()
        if month >= 1 and month <= 12:
            pass
        else:
            return ('wrong date')
        if day >= 1 and day <= 30 and month in [4, 6, 9, 11]:
            pass
        elif day >= 1 and day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
            pass
        # для високосного не делала
        elif day >= 1 and day <= 28 and month == 2:
            pass
        else:
            return 'wrong date'
        # год сделала до нашего времени
        if year >= 1 and year <= 2021:
            pass
        else:
            return 'wrong date'
        return 'date is alright'



print(Date.date_to_number())
a = Date('02.07.2021')
print(a.date_to_number())
print(Date.date_valid())
