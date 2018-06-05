import pytest
import time


def test_case_longtime_3second():
    time.sleep(3)
    assert 3 == 3


def test_case_longtime_2second():
    time.sleep(2)
    assert 3 == 3


def test_case_longtime_1second():
    time.sleep(1)
    assert 1 == 1
