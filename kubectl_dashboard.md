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

## create secret

```bash
> kubectl create secret generic kubernetes-dashboard-certs --from-file=/tmp/kubernetes-dashboard.crt -n kube-system
```

## delete secret

```bash
> kubectl delete  secret kubernetes-dashboard-certs -n kube-system
```

## delete old dashboard pod

```bash
> kubectl -n kube-system delete $(kubectl -n kube-system get pod -o name | grep dashboard)
```

## create secret

- pass

## aplly last dashboard

```bash
>
```

## start proxy

```

```

## or nodeport

[from her](https://github.com/kubernetes/dashboard/wiki/Accessing-Dashboard---1.7.X-and-above)

## edit interface type from ClusterIp to NodePort

```bash
> kubectl -n kube-system edit service kubernetes-dashboard
```

## show nodePort mapping

```bash
kubectl -n kube-system get service kubernetes-dashboard
```

## get master ip for cluster

```bash
> kubectl cluster-info
```

## call dashboard direct

```bash
curl https://<master-ip>:<nodePort>
# e.g. curl https://master-ip:nodeport
curl https://192.168.99.100:30000
```

## curl: (35) gnutls_handshake() failed: An unexpected TLS packet was received.

- cURL can NOT found the certificate for this connection

### debug cURL

```bash
> curl -vvv  https://192.168.99.100:30000
```

### show opensll

```bash
> openssl s_client-connect 192.168.99.100:30000
```

https://curl.haxx.se/docs/sslcerts.html

curl --cert /tmp/kubernetes-dashboard.crt https://192.168.99.100:30000

## kez for minikube

- [from here](https://github.com/kubernetes/minikube/issues/609)

- HINT:

- apple

```bash
curl https://192.168.99.100:8443/apis --key /Users/$USER/.minikube/certs/ca-key.pem --cert /Users/$USER/.minikube/certs/cert.pem --cacert /Users/$USER/.minikube/certs/ca.pem --cert-type PEM
```

- linux

```bash
curl -l https://192.168.99.100:8443/apis --key $HOME/.minikube/certs/ca-key.pem --cert $HOME/.minikube/certs/cert.pem --cacert $HOME/.minikube/certs/ca.pem --cert-type PEM

# with p12 format
# OSX's built-in cURL uses Apple's own Secure transport library instead of OpenSSL, and so only P12 format certificates are supported
```

## convert to p12 format

```bash
> openssl pkcs12 -export -in $HOME/.minikube/certs/cert.pem -inkey $HOME/.minikube/certs/key.pem -out $HOME/.minikube/certs/ca-key.p12
# without pasword -out newkey-no-pass.pem
# see here https://unix.stackexchange.com/questions/139110/expect-script-remove-password-on-private-key
touch noPasswd.txt|openssl pkcs12 -export -passin file:./noPasswd.txt -in $HOME/.minikube/certs/cert.pem -inkey $HOME/.minikube/certs/key.pem -out $HOME/.minikube/certs/ca-key.p12
```

## show crt path

```bash
kubectl config view
```
