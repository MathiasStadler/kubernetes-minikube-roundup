def print_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


print_kwargs(1, 3, 4, kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
