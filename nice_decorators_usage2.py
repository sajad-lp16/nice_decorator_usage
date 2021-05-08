# Author Sajad

import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG)


def decorator(level=logging.DEBUG, name=None, msg=None):
    """Executes a log as the function called"""

    def inner_decorator(func):
        log_name = name if name else func.__module__
        log_msg = msg if msg else func.__name__
        log = logging.getLogger(log_name)

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

        return wrapper

    return inner_decorator


@decorator(logging.DEBUG, "Sample", "Test_message")
def counter(n):
    while n < 5000:
        n += 1
    print(n)

# Only function will run after this
# counter.__wrapped__(1)

# both function and decorator will run
counter(1)
