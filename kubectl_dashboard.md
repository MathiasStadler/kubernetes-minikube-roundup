# [kubernetes dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

## [Remote HTTPS Accessing Kubernetes (kubectl) Dashboard 1.7.X and above](https://github.com/kubernetes/dashboard/wiki/Accessing-Dashboard---1.7.X-and-above)

https://github.com/kubernetes/dashboard/wiki/Installation#recommended-setup
https://github.com/kubernetes/dashboard/blob/master/README.md#getting-started

## Access Control guide

https://github.com/kubernetes/dashboard/wiki/Access-control

## Apply the latest Dashboard not install by default

- In most of the use cases you need to execute the following command to deploy latest development release:

```bash
> kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard-head.yaml
secret "kubernetes-dashboard-certs" configured
serviceaccount "kubernetes-dashboard-head" created
role.rbac.authorization.k8s.io "kubernetes-dashboard-minimal-head" created
rolebinding.rbac.authorization.k8s.io "kubernetes-dashboard-minimal-head" created
deployment.apps "kubernetes-dashboard-head" created
service "kubernetes-dashboard-head" created
```

## Recommended setup [copy and paste from here](https://github.com/kubernetes/dashboard/wiki/Installation#recommended-setup)

- To access Dashboard directly (without kubectl proxy) valid certificates should be used to establish a secure HTTPS connection. They can be generated using public trusted Certificate Authorities like Let's Encrypt. Use them to replace the auto-generated certificates from Dashboard.

- This setup requires, that certificates are stored in a secret named kubernetes-dashboard-certs in kube-system namespace. Assuming that you have dashboard.crt and dashboard.key files stored under $HOME/certs directory, you should create secret with contents of these files:

```bash
kubectl create secret generic kubernetes-dashboard-certs --from-file=$HOME/certs -n kube-system
```

- Afterwards, you are ready to deploy Dashboard using the following command:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
```

### self-signed certificates for kubernetes-dashboard-certs

[see here](https://github.com/kubernetes/dashboard/wiki/Certificate-management)

## call dashboard

```bash
> https://<master-ip>:<apiserver-port>/ui
# e.g.
> https://192.168.178.33:8080/ui
# if you get a error TRY this URL
> http://192.168.178.33:8080/api/v1/namespaces/kube-system/services/http:kubernetes-dashboard:/proxy/#!/node?namespace=default
```

## at this error

```txt
Error: 'tls: oversized record received with length 20527'
Trying to reach: 'https://172.17.0.2:9090/'
```

- delete the 's' fro https maybe you used minikube see the last link above
