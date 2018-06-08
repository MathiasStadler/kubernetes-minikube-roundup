# from here
# https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators

from functools import wraps


def wrap_in_tag(tag):
    def factory(func):
        @wraps(func)
        def decorator():
            return '<%(tag)s>%(rv)s</%(tag)s>' % (
                {'tag': tag, 'rv': func()})
        return decorator
    return factory


@wrap_in_tag('html')
@wrap_in_tag('b')
@wrap_in_tag('i')
def say():
    return 'hello'


print(say())


# version without @wraps(fn)

class sty(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, f):
        def newf():
            return "<{tag}>{res}</{tag}>".format(res=f(), tag=self.tag)
        return newf


@sty('b')
@sty('i')
def sayhi():
    return 'hi'


print(sayhi)
