
def log(expr=None):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            func_str = func.__name__
            args_str = ', '.join(args)
            kwargs_str = ', '.join([':'.join([str(j) for j in i])
                                    for i in kwargs.items()])
            print("Name => {}".format(func_str))
            print("args => {}".format(args_str))
            print("kwargs=> {}".format(kwargs_str))

            print("decorator expr {}".format(expr))

            with open('log.txt', 'w') as f:
                f.write(func_str)
                f.write(args_str)
                f.write(kwargs_str)
            print("Before calling " + func.__name__)
            output = func(*args, **kwargs)
            print("Before calling " + func.__name__)
            return output
        return wrapper
    return log_decorator


'''decorator with argument'''


@log("info")
def foo(x="Hello", y="Python"):
    print("{} {}".format(x, y))


'''decorator w/o argument'''


@log()
def baa(x="Hello", y="Python"):
    print("{} {}".format(x, y))


foo()
foo("Hallo")

baa("Hello")
