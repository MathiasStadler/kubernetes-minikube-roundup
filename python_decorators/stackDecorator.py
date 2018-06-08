# from here
# https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators

# The decorator to make it bold


def decorator1(fn):
    # The new function the decorator returns
    def wrapper():
        print("Before calling {}".format(fn.__name__))
        # Insertion of some code before and after
        result = fn()
        print("After calling {}".format(fn.__name__))
        return result
    return wrapper


def log(expr=None):
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            func_str = func.__name__
            args_str = ', '.join(args)
            kwargs_str = ', '.join([':'.join([str(j) for j in i])
                                    for i in kwargs.items()])
            print ("Log with Level {}".format(expr))
            print ("Name => {}".format(func_str))
            print ("args => {}".format(args))
            print ("kwargs=> {}".format(kwargs_str))

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


@log()
@decorator1
def foo():
    return "hello"


print(foo())
# outputs: <b><i>hello</i></b>


@log("info")
@decorator1
def baa():
    return "hello"


print(baa())
