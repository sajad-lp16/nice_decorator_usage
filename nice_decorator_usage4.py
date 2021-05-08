# Author Sajad

from functools import wraps


# useful example of decorators inside a class
class Sample(object):
    """
    We declare useful decorators
    inside this class then we can
    use them any where
    """

    @staticmethod
    def decorate(func):
        @wraps(func)
        def inner_decorate(*args, **kwargs):
            print("This is the first decorator")
            return func(*args, **kwargs)

        return inner_decorate

    @staticmethod
    def second_decorate(func):
        @wraps(func)
        def inner_decorate(*args, **kwargs):
            print("This is the second decorator")
            return func(*args, **kwargs)

        return inner_decorate


@Sample.decorate
def decorated():
    pass


decorated()