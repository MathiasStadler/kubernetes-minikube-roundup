# kubectl [secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

## get

```bash
> kubectl get secrets
# with namespace
> kubectl -n kube-system get secrets
```

## descript

```bash
> kubectl describe secrets/default-token-b2fr9
# with name
> kubectl -n kube-system describe secrets/kubernetes-dashboard-certs
```
