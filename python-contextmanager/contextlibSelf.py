from contextlib import ContextDecorator


class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        print("str => " + self.__str__())
        print(self.__getattribute__)
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False


@mycontext()
def function():
    print('The bit in the middle')


function()
