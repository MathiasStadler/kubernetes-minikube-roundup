# from here
# https://stackoverflow.com/questions/49210552/how-to-provide-args-and-kwargs-to-call-using-abbreviated-notation-of-clas


class MyDecoratorClass:
    def __init__(self, *args, **kwargs):
        # We store the arguments
        self.args = args
        self.kwargs = kwargs

        # Any other code that is needed here

    def __call__(self, fun_to_decorate):  # Single argument
        def inner(*args, **kwargs):

            # Here you have access to self.args and self.kwargs

            print("fn => ")

            return fun_to_decorate(*args, **kwargs)

        return inner


@MyDecoratorClass
def callD():
    print ("Hello callD")


print(callD)
