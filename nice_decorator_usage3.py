# Author Sajad

from functools import wraps
import time
import os


def decorate(func):
    @wraps(func)
    def wrapper(file=None,**kwargs):
        try:
            t1 = time.time()
            name = kwargs['file_name']
            file = open(name, 'r')
            func(file)
            t2 = time.time()
            file.close()
        except FileNotFoundError:
            print(os.getcwd())
            print('file was not found')
        except IOError:
            print('couldnt find target')
        except Exception as e:
            print(e)
        else:
            print(t2-t1)
        finally:
            if file and not file.closed:
                file.close()
    return wrapper


@decorate
def func(file=None, **kwargs):
    file.readlines()


func(file=None,file_name='temp.txt')