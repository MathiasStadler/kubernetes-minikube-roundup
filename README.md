<!-- markdownlint-disable MD041 -->
> I would greatly appreciate it if you kindly give me some feedback if you found an error
> [Send feedback to me](mailto:feedback@mathias-stadler.de)
<!-- markdownlint-enable MD041 -->

# kubernetes-minikube-roundup

## check VMX on MAC

```bash
> sysctl -a | grep machdep.cpu.features | grep VMX
machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PATPSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMXSMX EST TM2 SSSE3 FMA CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC MOVBE POPCNT AES PCID XSAVE OSXSAVE SEGLIM64 TSCTMR AVX1.0 RDRAND F16C
```

- minikube run local with Oracle VirtualBox

## only for my thought and other things

## wrap up exits installation on OS X hosts

TODO check with install

```bash
minikube stop
minikube delete
docker stop $(docker ps -aq)
rm -rf ~/.kube ~/.minikube

sudo rm -rf /usr/local/bin/kubectl /usr/local/bin/minikube
systemctl stop '*kubelet*.mount'
sudo rm -rf /etc/kubernetes/
docker system prune -af --volumes
brew uninstall kubectl
brew uninstall kubernetes-helm
brew cask uninstall minikube
```

## install minikube on apple / MacOS

- We will use the variant with Oracle VirtualBox for Apple

## Install VirtualBox for Apple

[Download Version OS X hosts and follow the Instruction](https://www.virtualbox.org/wiki/Downloads)

## update brew

- [install brew](https://brew.sh/) if you not already done, follow the instruction of the site

- usually way to install brew

```bash
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```bash
brew update
```

## install kubectl

- cli tool for control the minikube cluster

- [deeper information](https://kubernetes.io/docs/tasks/tools/install-kubectl/#before-you-begin)

```bash
> brew install kubectl
```

- validate installation

```bash
> kubectl version
```

- the output should look like

```bash
08:54 $ kubectl version
Client Version: version.Info{Major:"1", Minor:"10", GitVersion:"v1.10.2", GitCommit:"81753b10df112992bf51bbc2c2f85208aad78335", GitTreeState:"clean", BuildDate:"2018-05-12T04:12:12Z", GoVersion:"go1.9.6", Compiler:"gc", Platform:"darwin/amd64"}
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

- don't worry about the refused connection, this is the next step

## install minikube

- [github minikube](https://github.com/kubernetes/minikube)
- [deeper information](https://kubernetes.io/docs/tasks/tools/install-minikube/)

```bash
> brew cask install minikube
```

## minikube start

-[details see here](https://kubernetes.io/docs/getting-started-guides/minikube/)

```bash
> minikube start
```

- start minikube with more power
- e.g 4 cpus, 4 gb ram on VirtualBox

```bash
minikube start --vm-driver=virtualbox --container-runtime=docker --cpus 4 --memory 4098
```

- with full loglevel

```bash
> minikube start --v=7 --logtostderr
```


## more than one minikube local

```bash
#start
> minikube start --profile=anotherminikube

#status
> minikube status --profile anotherminikube

#stop
> minikube stop --profile anotherminikube

# set anotherminikube to default
# Result: minikube command without profile flag use this one
> minikube config set PROPERTY_NAME PROPERTY_VALUE
> minikube config set profile anotherminikube

# check which minikube is default
> n get profile

# delete
minikube delete --profile anotherminikube

```

## minikube show profile/machines

```bash
ls -l  ~/.minikube/machines/ |grep ^d
```

## minikube start [flags]

```bash
Usage:
  minikube start [flags]

Flags:
      --apiserver-ips ipSlice          A set of apiserver IP Addresses whichare used in the generated certificate for localkube/kubernetes.  This can beused if you want to make the apiserver available from outside the machine (default [])
      --apiserver-name string          The apiserver name which is used in the generated certificate for localkube/kubernetes.  This can be used if you want to make the apiserver available from outside the machine (default "minikubeCA")
      --apiserver-names stringArray    A set of apiserver names which are used in the generated certificate for localkube/kubernetes.  This can be used if you want to make the apiserver available from outside the machine
      --cache-images                   If true, cache docker images for the current bootstrapper and load them into the machine. (default true)
      --container-runtime string       The container runtime to be used
      --cpus int                       Number of CPUs allocated to the minikube VM (default 2)
      --disable-driver-mounts          Disables the filesystem mounts provided by the hypervisors (vboxfs, xhyve-9p)
      --disk-size string               Disk size allocated to the minikube VM (format: <number>[<unit>], where unit = b, k, m or g) (default "20g")
      --dns-domain string              The cluster dns domain name used in the kubernetes cluster (default "cluster.local")
      --docker-env stringArray         Environment variables to pass to the Docker daemon. (format: key=value)
      --docker-opt stringArray         Specify arbitrary flags to pass to the Docker daemon. (format: key=value)
      --extra-config ExtraOption       A set of key=value pairs that describe configuration that may be passed to different components.
                The key should be '.' separated, and the first part before the dot is the component to apply the configuration to.
                Valid components are: kubelet, apiserver, controller-manager, etcd, proxy, scheduler.
      --feature-gates string           A set of key=value pairs that describe feature gates for alpha/experimental features.
  -h, --help                           help for start
      --host-only-cidr string          The CIDR to be used for the minikube VM (only supported with Virtualbox driver) (default "192.168.99.1/24")
      --hyperv-virtual-switch string   The hyperv virtual switch name. Defaults to first found. (only supported with HyperV driver)
      --insecure-registry strings      Insecure Docker registries to pass to the Docker daemon.  The default service CIDR range will automatically be added.
      --iso-url string                 Location of the minikube iso (default"https://storage.googleapis.com/minikube/iso/minikube-v0.26.0.iso")
      --keep-context                   This will keep the existing kubectl context and will create a minikube context.
      --kubernetes-version string      The kubernetes version that the minikube VM will use (ex: v1.2.3)
 OR a URI which contains a localkube binary (ex: https://storage.googleapis.com/minikube/k8sReleases/v1.3.0/localkube-linux-amd64) (default "v1.10.0")
      --kvm-network string             The KVM network name. (only supported with KVM driver) (default "default")
      --memory int                     Amount of RAM allocated to the minikube VM in MB (default 2048)
      --mount                          This will start the mount daemon and automatically mount files into minikube
      --mount-string string            The argument to pass the minikube mount command on start (default "/Users:/minikube-host")
      --network-plugin string          The name of the network plugin
      --nfs-share strings              Local folders to share with Guest viaNFS mounts (Only supported on with hyperkit now)
      --nfs-shares-root string         Where to root the NFS Shares (defaults to /nfsshares, only supported with hyperkit now) (default "/nfsshares")
      --registry-mirror strings        Registry mirrors to pass to the Docker daemon
      --vm-driver string               VM driver is one of: [virtualbox vmwarefusion kvm xhyve hyperv hyperkit kvm2 none] (default "virtualbox")
      --xhyve-disk-driver string       The disk driver to use [ahci-hd|virtio-blk] (only supported with xhyve driver) (default "ahci-hd")

Global Flags:
      --alsologtostderr                  log to standard error as well as files
  -b, --bootstrapper string              The name of the cluster bootstrapper that will set up the kubernetes cluster. (default "kubeadm")
      --log_backtrace_at traceLocation   when logging hits line file:N, emita stack trace (default :0)
      --log_dir string                   If non-empty, write log files in this directory
      --loglevel int                     Log level (0 = DEBUG, 5 = FATAL) (default 1)
      --logtostderr                      log to standard error instead of files
  -p, --profile string                   The name of the minikube VM being used.
        This can be modified to allow for multiple minikube instances to be run independently (default "minikube")
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          log level for V logs
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
```

## minikube config

```bash
> cat ~/.minikube/machines/minikube/config.json
```

## minikube status

```bash
> minikube status
```

- the output should look like

```bash
> minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.105
```

- for control the cluster will we use kubectl
- kubectl cluster-info should give us the same information

```bash
kubectl cluster-info
Kubernetes master is running at https://192.168.99.105:8443
KubeDNS is running at https://192.168.99.105:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

## minikube start/stop/status/delete

- stop

```bash
> minikube stop
```

- check status

```bash
> $ minikube status
minikube: Stopped
cluster:
kubectl:
```

- start

```bash
> minikube start
```

- check status

```bash
$ minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.105
```

- minikube delete

```bash
minikube delete
```

## show all versions of minikube

```bash
> minikube get-k8s-versions
```

## start different version of minikube

```bash
> minikube start --kubernetes-version v1.7.3 --profile=mkv173
```

## get ip from minikube

```bash
> minikube get ip
```

## get ip of minikube

```bash
> minikube ip
```

## deploy hello-minikube on cluster

[from here](https://kubernetes.io/docs/getting-started-guides/minikube/#kubectl)

> kubectl: Is the cli program for control a kubernetes cluster local/remote
> **Think on your production**
> check minikube status AND kubectl cluster-info print the same IP addr before you start

```bash
> minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
> kubectl cluster-status
Kubernetes master is running at https://192.168.99.100:8443
```

```bash
> kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.4 --port=8080
```

## minikube version

```bash
> minikube version
```

## minikube network access checking

```bash
> minikube ssh curl http://www.google.com
```

## docker

```bash
> echo $(minikube docker-env)
> eval $(minikube docker-env)
> docker info
```


## minikube issue

[error report ](https://github.com/kubernetes/minikube/issues/2472)

```bash
> minikube start --kubernetes-version=https://github.com/kubernetes/minikube/releases/download/v0.25.0/localkube
```

## install minikube version  v0.25.2 from brew cask

- All credits goes to [Joeri Verdeyen - Downgrade an application installed with Brew Cask article](https://www.jverdeyen.be/mac/downgrade-brew-cask-application/)

```bash
> brew cask install https://raw.githubusercontent.com/minikube-bot/homebrew-cask/3c2839b870b40b78663c678b33352e370260114c/Casks/minikube.rb
```

## Kubernetes master is running at https://192.168.99.101:8443 getsockopt: network is unreachable

- Solution Version 0.26.1 is the binary localkube not available

## localkube start/stop/status

- main service of minikube

```bash
> minikube ssh sudo systemctl stop localkube

> minikube ssh sudo systemctl start localkube

> minikube ssh sudo systemctl status
 localkube
```

## sources

[](https://gist.github.com/kevin-smets/b91a34cea662d0c523968472a81788f7)


## Troubles1hooting

- view status of VBoxNet interfaces

```bash
> VBoxManage list hostonlyifs
```

interface not up
https://www.virtualbox.org/ticket/16911

# host-only network
[Erklärung Host-only network german](https://www.thomas-krenn.com/de/wiki/Netzwerkkonfiguration_in_VirtualBox#Host-only_networking)

## proplem with double VirtualBox Host network

vboxnet0:
vboxnet1: