"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)

"""
from functools import wraps
# Вариант 1
def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        args_list = []
        for arg in args:
            args_list.append((arg, type(arg)))
        return args_list, type(func_result)
    return wrapper

@type_logger
def calc_cube(*args):
    """some info how to calc_cube"""
    args_calc_list = [arg ** 3 for arg in args]
    return args_calc_list

print(calc_cube(5, 6, 7))

# Вариант 2 с выводом имени функции
def type_logger_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        args_list = []
        for arg in args:
            string_arg = f'{func.__name__}({arg}, {type(arg)})'
            args_list.append(string_arg)
        return args_list, type(func_result)
    return wrapper

@type_logger_1
def calc_cube_1(*args):
    """some info how to calc_cube_1"""
    args_calc_list = [arg ** 3 for arg in args]
    return args_calc_list

print(calc_cube_1(5, 6, 7))
print(calc_cube.__name__)
print(calc_cube.__doc__)
print(calc_cube_1.__name__)
print(calc_cube_1.__doc__)

# Вариант 3 с именованным аргументом
def type_logger_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        args_list = []
        for arg in args:
            string_arg = f'{func.__name__}({arg}, {type(arg)}, {kwargs})'
            args_list.append(string_arg)
        return args_list, type(func_result)
    return wrapper

@type_logger_2
def calc_cube_2(*args, degree = 1):
    """some info how to calc_cube_2"""
    args_calc_list = [arg ** degree for arg in args]
    return args_calc_list

print(calc_cube_2(5, 6, 7, degree = 3))
print(calc_cube_2.__name__)
print(calc_cube_2.__doc__)
