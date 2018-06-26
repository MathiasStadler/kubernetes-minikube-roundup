# kubectl-grafana

```txt
https://github.com/grafana/kubernetes-app
```

## overview pictures about influxdb

[see here](https://www.influxdata.com/time-series-platform/chronograf/mini)

## install

- e.g. I'm follow this here

```bash
cd ~/playground
git clone https://github.com/kubernetes/heapster.git
cd heapster
cd /deploy/kube-config/influxdb

# EDIT remove thr comment sign in grafana.yaml in the  nodeport line

# DON*t forget to edit the hostpath inside the influxdb.yaml
```

## show services

```bash
kubectl describe service monitoring-grafana --namespace=kube-system

kubectl get services -n kube-system | grep influxdb
```

## inside

```txt
https://github.com/kubernetes/dashboard/issues/2259
or
https://victorpalau.net/2016/08/02/deploying-heapster-to-kubernetes/
```

## heapster keys

- /metrics contains lots of metrics in Prometheus format that can indicate the root cause of Heapster problems.
- [from here](https://github.com/kubernetes/heapster/blob/master/docs/debugging.md)

> ip found you via **kubectl get services** command

```bash
# run inside minikube
# minikube ssh
> curl 10.111.66.23:80/metrics
```

- **/api/v1/model/debug/allkeys** has a list of all metrics sets that are processed inside Heapster. This can be useful to check what is passed to your configured sinks Example:

```bash
> curl 10.111.66.23:80/api/v1/model/debug/allkeys
```

## log heapster

```bash
kubectl logs --namespace=kube-system -v 9  $(kubectl get pods --namespace=kube-system |grep heapster |awk '{print $1}'

kubectl logs --namespace=kube-system -v 9  $(_TO_LOG_SERVICE="heapster";kubectl get pods --namespace=kube-system |grep ${_TO_LOG_SERVICE} |awk '{print $1}')
```

## influxdb log

```bash
kubectl logs --namespace=kube-system -v 9  $(_TO_LOG_SERVICE="influxdb";kubectl get pods --namespace=kube-system |grep ${_TO_LOG_SERVICE} |awk '{print $1}')
```

## influxe ping

```bash
# ping anonym
# Stcurl -G 'http://localhost:8086/query?db=mydb' --data-urlencode 'q=SELECT * FROM "mymeas"'atus 204 Success! Your InfluxDB instance is up and running.
> curl -sl -I 10.106.48.248:8086/ping

# debug request 60 sec
> curl -vvv 10.106.48.248:8086/debug/requests?seconds=60


# show all databases
curl -G "http://10.106.48.248:8086/query?pretty=true" --data-urlencode "q=SHOW DATABASES"

curl -G "http://10.106.48.248:8086/query?pretty=true" --data-urlencode "q=SHOW SERIES ON k8s"


# check db via curl
> curl -G 'http://10.106.48.268:8086/query?db=influxdb-datasource' --data-urlencode 'q=SELECT * FROM "mymeas"'
```

## log grafana

```bash
kubectl logs --namespace=kube-system -v 9  $(_TO_LOG_SERVICE="grafana";kubectl get pods --namespace=kube-system |grep ${_TO_LOG_SERVICE} |awk '{print $1}')
```

## access influxdb

```bash

```

## trouble shouting

```txt
reflector.go:190] k8s.io/heapster/metrics/util/util.go:30: Failed to list *v1.Node: nodes is forbidden: User "system:serviceaccount:kube-system:heapster" cannot list nodes at the cluster scope
```

### see here

```txt
https://github.com/kubernetes/kubeadm/issues/248
```

### fix

- add a role

```bash
kubectl create clusterrolebinding add-on-cluster-admin \
    --clusterrole=cluster-admin \
    --serviceaccount=kube-system:default
```

- restart heapster

- restart pod if you have no yaml file
- [from here](https://stackoverflow.com/questions/40259178/how-to-restart-kubernetes-pods)

```bash
kubectl get pod PODNAME -n NAMESPACE -o yaml | kubectl replace --force -f -

kubectl get pod $(kubectl get pods --namespace=kube-system |grep heapster |awk '{print $1}') -n kube-system -o yaml | kubectl replace --force -f -
```
