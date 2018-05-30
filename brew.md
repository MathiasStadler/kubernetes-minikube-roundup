# brew housekeeping

- [brew FAQ](https://docs.brew.sh/FAQ)

## show install brew formula

```bash
> brew list
> brew list --versions
```

## save and install all brew formula

```bash
# 1st step generate list and store at file
> brew list > Brewfile
# 2nd step e.g. on another instance
> cat Brewfile |xargs brew install
# Additional step upgrade formula
> cat Brewfile|xargs brew upgrade
```