"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
125
#>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?

"""

from functools import wraps

def val_checker(condidtion_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            _val_result = condidtion_func(*args)
            if not _val_result:
                raise ValueError(f'wrong val: {args}')
            else:
                 return func(*args)
        return wrapper
    return _val_checker

#сделаем контрольную функцию и передадим ее как аргумент
def check_func(x):
    return x > 0

#@val_checker(lambda x: x > 0)
@val_checker(check_func)
def calc_cube(x):
    """some info about calc"""
    return x ** 3

print(calc_cube(5))
#print(calc_cube(-5))
print(calc_cube.__name__)
print(calc_cube.__doc__)




