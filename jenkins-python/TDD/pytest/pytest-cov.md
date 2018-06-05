# [pytest-cov](https://github.com/pytest-dev/pytest-cov/)

- coverage with pytest and coverage.py

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
```

## check pytest-cav

```bash
> py.test --cov=myproj tests/
```

## article about pytest-cov

- [quick inducement](https://www.robinandeer.com/blog/2016/06/22/how-i-test-my-code-part-3/)
