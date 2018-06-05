# [pytest](https://github.com/pytest-dev/pytest)

## version

```bash
> py.test --version
```

## install pytest

```bash
> pip3 install pytest
```

## print stdout

```bash
> py.test -s
```

## py.test help

```bash
> py.test --help
> py.test -help
```

## stopping test after first or n failures

```bash
# stop after the first fail test case
> py.test --maxfail 1
 test/test_maxfail.py
# stop after the third fail test case
> py.test --maxfail 3
```

## run test

- run all test in the same directory and sub directory
- py.test will discovery and automatically run all tests

```bash
> py.test
> py.test -v
> py.test --verbose
```

- run all test inside directory test

```bash
> py.test test
```

- run all test in verbose mode in sub directory test

```bash
> py.test --verbose
> py.test -v test
```

- run a single test module

```bash
> py.test -v test/test_module2.py
```

- run a specific test class inside test module

```bash
> py.test -v test/test_module02.py::TestClass01::test_case01
```

## py.test raises

```python
import pytest

# pytest.raises expect an exception

# successful because we have a exception,  1/0 is an error division by null
def test_case01():
    with pytest.raises(Exception):
        x = 1 / 0

# fail because we have NOT a exception, 1/1 is 1 NOT exception
def test_case02():
    with pytest.raises(Exception):
        x = 1 / 1
```

## test profile

- show the slowest n test durations

- show the slowest 3 test in directory test

```bash
> py.test -v --durations=10  test/test_longtime.py
```

- e.g [test_longtime.py](test/test_longtime.py)

## generated junit / xunit xml log

```bash
>
py.test --junitxml=result.xml
```

## generated plain result log

- result-log is **deprecated** and scheduled for removal in pytest 4.0.
  > - [See](https://docs.pytest.org/en/latest/usage.html#creating-resultlog-format-files) for more information.
  > - An alternative for users which still need similar functionality is to use the [pytest-tap](https://pypi.org/project/pytest-tap/) plugin which provides a stream of test data.
  > - pytest-tap is a reporting plugin for pytest that outputs Test Anything Protocol (TAP) data. TAP is a line based test protocol for recording test data in a standard way.
  > - [github pytest-tap](https://github.com/python-tap/pytest-tap)

```bash
> py.test ----resultlog=result.log
```

## coverage with pytest => [pytest-cov](https://github.com/pytest-dev/pytest-cov/)

### install
