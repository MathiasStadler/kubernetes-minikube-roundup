class decorator2:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()


@decorator2
def foo():
    print("inside foo()")


foo()


# with decorators argument
class sty(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, f):
        def newf(*args, **kwargs):
            print("fn => {}".format(f.__name__))
            # We store the arguments
            self.args = args
            self.kwargs = kwargs
            args_str = ', '.join(args)
            kwargs_str = ', '.join([':'.join([str(j) for j in i])
                                    for i in kwargs.items()])

            print ("args => {}".format(args_str))

            print ("kwargs=> {}".format(kwargs_str))

            return "<{tag}>{res}</{tag}>".format(res=f(*args, **kwargs), tag=self.tag)
        return newf


@sty('hml')
@sty('b')
@sty('i')
def sayhi(x=None, y="hallo"):
    return 'hi'


print(sayhi("hallo"))
