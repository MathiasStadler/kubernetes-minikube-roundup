# from here
# https://www.python-course.eu/python3_decorators.php


class A:

    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)


print("Hallo")
x = A()

x("hallo", 2, None, 3, 4, 5)
