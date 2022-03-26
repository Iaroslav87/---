"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
"""

from functools import wraps

def val_checker(decorator_check_fune):
    def _val_checker(func_calc_cube):
        @wraps(fune_calc_cube)
        def wrapped(x):
            if decorator_check_fune(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)
        return wrapped
    return _val_checker
@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
