# from here
# https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d


import sys
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print (method.__name__)
        print(int((te - ts) * 1000))

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print (method.__name__)
            print ("{} {} ms ".format(method.__name__, int((te - ts) * 1000)))
        return result

    return timed


@timeit
def test_timed():
    time.sleep(1)


test_timed()


@timeit
def test1_timed(log_time=None):
    time.sleep(1)
