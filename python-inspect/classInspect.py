# from here
# https://docs.python.org/3/library/inspect.html

import inspect


def gen():
    yield


@types.coroutine
def gen_coro():
    yield


assert not isawaitable(gen())
assert isawaitable(gen_coro())
