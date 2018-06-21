# update go on ubuntu

- [mainly from here](https://askubuntu.com/questions/720260/updating-golang-on-ubuntu)

```bash
> sudo apt-get purge golang*

# ups nothing to delete
# we use gvm :-)
```

## use [gvm](https://github.com/moovweb/gvm) - Go Version Manager

- installation see github page

```bash
# list installed go version
> gvm list
# list all avaible go version
> gvm listall
# switch the dafault go version
> gvm use go1.9.7 --default
# cool nice tool
```
