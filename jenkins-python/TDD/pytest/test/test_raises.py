import pytest

# pytest.raises expect a exception

# successful because we have a exception 1/0 is an error


def test_case01():
    with pytest.raises(Exception):
        x = 1 / 0
        print("x => $i" % x)

# successful because we have NOT a exception 1/1 is 1 NOT exception


def test_case02():
    with pytest.raises(Exception):
        x = 1 / 1
        print("x => %i" % x)
