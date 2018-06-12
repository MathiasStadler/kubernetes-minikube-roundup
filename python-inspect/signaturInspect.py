from inspect import signature


def foo(a, *, b: int, **kwargs):
    pass


sig = signature(foo)

print(str(sig))

print(str(sig.parameters['b']))
print(str(sig.parameters['a']))
print(sig.parameters['b'].annotation.__name__)


def test(a, b):
    pass
    sig = signature(test)
    new_sig = sig.replace(return_annotation="new return anno")

    print(str(new_sig))


test("a", "b")


# class MySignature(Signature):
#    pass

# sig = MySignature.from_callable(min)
# assert isinstance(sig, MySignature)


def foo(a, b, *, c, d=10):
    pass


sig = signature(foo)
for param in sig.parameters.values():
    if (param.kind == param.KEYWORD_ONLY and
            param.default is param.empty):
        print('Parameter:', param)
