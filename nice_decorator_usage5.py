# Author Sajad

import functools
import logging

# initial configurations
logging.basicConfig(level=logging.DEBUG)


# As the interpreter reaches this function(decorator below) it runs is
# So it has to return callable thing i sat a partial in order to return
# uncalled function to avoid unlimited recursion

def attach_wrapper(obj, func=None):
    if func is None:
        return functools.partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def decorator(level, name, msg):
    def inner_decorator(func):
        log_name = name if name else func.__module__
        log_msg = msg if msg else func.__name__
        log = logging.getLogger(log_name)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_message):
            nonlocal log_msg
            log_msg = new_message

        return wrapper

    return inner_decorator


@decorator(logging.DEBUG, 'Sample', 'Test Message')
def counter(n):
    while n < 50000:
        n += 1


# Changing logger message
# counter.set_message("What")

# Changing logger level
# counter.set_level(logging.WARNING)
