# kubectl-ssl

```txt
# connect https
cd ~/.minikube/certs
curl -v -k --cacert ./ca.pem --key ./key.pem --cert ./cert.pem https://192.168.99.102:8443/api/v1/namespaces/kube-system/service
```

## https connect as user

- find the client keys in the output of

```txt
kubectl config view
```

## connect http

## connect Bearer Token

- [from here](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/)

```bash
APISERVER=$(kubectl config view | grep server | cut -f 2- -d ":" | tr -d " ")
TOKEN=$(kubectl describe secret $(kubectl get secrets | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t')
curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
```

## other

```bash
curl -v http://192.168.99.102:8443/api/v1
```

- URL from kubectl cluster-info
