# from here
# https://www.python-course.eu/python3_decorators.php


def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            # func(x)
            func(x)
        return function_wrapper
    return greeting_decorator


@greeting("Hallo foo")
def foo(x):
    print(42)


@greeting("Hallo Alice")
def alice(x):
    print(66)


# greeting2 = greeting("Hallo Argument")
# foo = greeting2(foo)
foo("Hi")
alice("hello")
