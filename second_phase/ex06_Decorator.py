# from functools import wraps
# from time import time
#
#
# def record_time(func):
#     """自定义装饰函数的装饰器"""
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         return result
#
#     return wrapper

from functools import wraps
from time import time


def record(output):
    """自定义带参数的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper

    return decorate


from functools import wraps
from time import time


class Record():
    """自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            self.output(func.__name__, time() - start)
            return result

        return wrapper