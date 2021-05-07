# Author : Sajad

from functools import wraps
import time
from inspect import Signature  # returns the annotation of a function


def dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_s = time.time()
        func(*args, **kwargs)
        t_e = time.time()
        print(func.__name__, t_e - t_s)

    return wrapper


@dec
def counter(n):
    while n < 500000:
        n += 1


#######################################
# This acts exactly like a decorator
# counter = dec(counter)
#######################################

# test the module
counter(2)

# This is an example in OOP

# class Oop:
#     # 1 @classmethod
#     # 1 def _class(cls):
#     # 1     pass
#
#     # 2def _class(cls):
#     # 2    pass
#     # 2
#     # 2_class = classmethod(_class)

# wraps decorator allows the decorated function to reach metadata (__name__,__class__,__doc__)

# Runs only function scope(unwrapping function)
counter.__wrapped__(5)


# Built in decorators support __func__ insted of __wrapped__


# An example of a decorator which accepts values
def dec2(arg1, arg2):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(arg1, arg2)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return inner_dec


@dec2('one', 'two')
def counter2(n=500):
    while n < 5000:
        n += 1
