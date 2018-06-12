from contextlib import contextmanager


def pseudo_log(msg):
    print("log => {}".format(msg))


@contextmanager
def tag(name):
    print("<%s>" % name)
  # not work   pseudo_log(yield)
    pseudo_log(name)
    print("</%s>" % name)


with tag("h1"):
    print("foo")
