import functools
import random


class cache(object):

    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):

        result = self.func(*args, **kwargs)

        return result


@cache
def function_to_wrap(bits=128):
    return random.getrandbits(bits)


if __name__ == "__main__":
    print(function_to_wrap())
    print(function_to_wrap())
