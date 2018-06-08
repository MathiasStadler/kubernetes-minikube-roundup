# from here
# https: // www.python-course.eu/python3_decorators.php


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling {}".format(func.__name__))
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))


print("We call foo before decoration:")
foo("Hi")

# print("We now decorate foo with f:")
#foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)
