# from here
# https://stackoverflow.com/questions/39078467/python-how-to-get-the-calling-function-not-just-its-name


import sys
import inspect


def get_calling_function():
    """finds the calling function in many decent cases."""
    fr = sys._getframe(1)   # inspect.stack()[1][0]
    co = fr.f_code
    for get in (
        lambda: fr.f_globals[co.co_name],
        lambda: getattr(fr.f_locals['self'], co.co_name),
        lambda: getattr(fr.f_locals['cls'], co.co_name),
        lambda: fr.f_back.f_locals[co.co_name],  # nested
        lambda: fr.f_back.f_locals['func'],  # decorators
        lambda: fr.f_back.f_locals['meth'],
        lambda: fr.f_back.f_locals['f'],
    ):
        try:
            func = get()
        except (KeyError, AttributeError):
            pass
        else:
            if func.__code__ == co:
                return func
    raise AttributeError("func not found")

# Usage


def f():
    def nested_func():
        print(get_calling_function())
    print(get_calling_function())
    nested_func()


class Y:
    def meth(self, a, b=10, c=11):
        print(get_calling_function())

        class Z:
            def methz(self):
                print(get_calling_function())
        z = Z()
        z.methz()
        return z

    @classmethod
    def clsmeth(cls):
        print(get_calling_function())

    @staticmethod
    def staticmeth():
        print(get_calling_function())


f()
y = Y()
z = y.meth(7)
z.methz()
y.clsmeth()
# y.staticmeth()  # would fail
