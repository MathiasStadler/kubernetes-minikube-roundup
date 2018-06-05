# [pytest-cov](https://github.com/pytest-dev/pytest-cov/)

- coverage with pytest and coverage.py

## [Documentation](http://pytest-cov.readthedocs.io/en/latest/)

## uninstall

- **make sure** you are uninstalled old version
- Upgrading from ancient pytest-cov

```txt
pytest-cov 2.0 is using a new .pth file (pytest-cov.pth). You may want to manually remove the older init_cov_core.pth from site-packages as it's not automatically removed.
```

```bash
> pip uninstall pytest-cov
> pip3 uninstall pytest-cov
```

## install

```bash
> pip3 install pytest-cov
> pip3 install --upgrade setuptools
> py.test --version
# You should see like that
This is pytest version 3.6.0, imported from /usr/local/lib/python3.6/site-packages/pytest.py
setuptools registered plugins:
  pytest-cov-2.5.1 at /usr/local/lib/python3.6/site-packages/pytest_cov/plugin.py
```

## check pytest-cav

```bash
> py.test --cov=mypackage myproject/tests/
# or alternative
> cd myproject
> py.test --cov=mypackage tests/
```

## term-missing

- display lines numbers in python file was not under coverage

```bash
py.test --cov-report term-missing --cov=mypackage myproject/tests/
```

## make report

```bash
py.test --cov-report html  \
        --cov-report xml   \
        --cov-report annotate   \
        --cov=mypackage myproject/tests/
```

> - **HINT** Show at the generated webpage for details information about was is and was is **NOT** coverage with your test

## article about pytest-cov

- [quick inducement](https://www.robinandeer.com/blog/2016/06/22/how-i-test-my-code-part-3/)
