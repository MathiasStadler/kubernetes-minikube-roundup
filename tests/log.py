def log(func):
    def wrapper(*args, **kwargs):
        func_str = func.__name__
        args_str = ', '.join(args)
        kwargs_str = ', '.join([':'.join([str(j) for j in i])
                                for i in kwargs.items()])
        with open('log.txt', 'w') as f:
            f.write(func_str)
            f.write(args_str)
            f.write(kwargs_str)
        return func(*args, **kwargs)
    return wrapper


@log
def example(a, b):
    print('example')


print(example("a", "b"))
