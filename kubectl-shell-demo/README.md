# [shell demo](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/

## yaml file with nigx image

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: shell-demo
spec:
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: nginx
    image: nginx
    volumeMounts:
    - name: shared-data
      mountPath: /usr/share/nginx/html
```

## deploy

```bash
> kubectl create -f .
```

## access to shell

```bash
> kubectl exec -it shell-demo -- /bin/bash
# exit
> exit
```
