# from here
# https://www.python-course.eu/python3_decorators.php


def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper


@call_counter
def succ(x):
    return x + 1


print(succ.calls)
for i in range(99):
    succ(i)

print(succ.calls)
