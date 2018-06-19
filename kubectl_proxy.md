# kubectl proxy

## ** DON'T USED kubectl proxy FOR PRODUCTION **

- [see here for the recommandation](https://github.com/kubernetes/dashboard/wiki/Installation#recommended-setup)

## status

```bash
> kubectl proxy
```

## allow remote access start as background proses

```bash
kubectl proxy --port=8080 --address 0.0.0.0 --accept-hosts '.*' &
```

## show job in the background

- [e.g. from here](https://www.computerhope.com/unix/ubg.htm)

```bash
# list n jobs in the background
> bg
# shoiw wich job in the background
> jobs
# bring last job in the foreground
> fg
```
