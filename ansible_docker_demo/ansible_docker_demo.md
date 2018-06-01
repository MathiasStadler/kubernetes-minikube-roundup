# [ansible_docker_demo](https://linuxacademy.com/howtoguides/posts/show/topic/13750-managing-docker-containers-with-ansible)

## copy private kez from vagrant to guest machine

* the vagrant-scp plugin must installed

```bash
> vagrant scp ~/.vagrant.d/insecure_private_key jenkins:/home/vagrant/.ssh/id_rsa
```

* test is login on guest machine via public key possible

```bash
# found ip of host
> hostname -I
# ssh should work with all
> ssh vagrant@127.0.0.1
```

## vagrant user used for this demo instead ubuntu

## ansible docker role for ubuntu and debian strech

[here](https://github.com/angstwad/docker.ubuntu)nc -zv 192.168.64.8 2375

## check listen docker deamon

```bash
nc -zv 192.168.64.8 2375
```

## iproute2 ss [command](https://www.cyberciti.biz/tips/linux-investigate-sockets-network-connections.html)

* display open listening TCP port

```bash
> ss -t -a
```
