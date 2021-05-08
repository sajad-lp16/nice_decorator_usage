# Author Sajad


# This is a metaclass wich creates the classes
# And control them while creation
class Meta(type):
    def __new__(meta, cls_name, bases, dic):
        args = (cls_name, bases, dic)
        return type(*args)


class Sample(object, metaclass=Meta)
    def __new__(cls, *args):  # args contain attribute names which
        return object.__new__(Sample)  # whey will quantify by init later

    def __init__(self, name):
        self.name = name


# in order to avoid inheritance
# we can declare functions this way

def Foo(object):
    pass


class Meta2(type):
    def __new__(meta, cls_name, bases, dic):
        args = (cls_name, bases, dic)
        return type(cls_name, (), dic)


# This will raise an Error
class Sample2(Foo, metaclass=Meta2):
    pass


# Avoid triangle inheritance !!!!
class Sample3(object, Foo):
    pass

# why? => Sample.__mro__ -> sample3 > object > Foo > object
# So we use object only if its the only class to inherit from
