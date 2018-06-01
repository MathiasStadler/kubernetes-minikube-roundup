# xxx

## ansible with docker

https://linuxacademy.com/howtoguides/posts/show/topic/13750-mmkdianaging-docker-containers-with-ansible

## install via api and token

https://github.com/buluma/ansible-role-jenkins/blob/master/tasks/plugins.yml

## ansible docker sample

```bash
24  mkdir ansible_docker_demo
   25  cd $_
   26  mkdir roles
   27  vi ansible.cfg
   28  export ANSIBLE_CONFIG=$(pwd)/ansible.cfg
   29  cat  $ANSIBLE_CONFIG
   30  ip a
   31  vi hosts
   32  export ANSIBLE_HOSTS=$(pwd)/hosts
   33  vi requirements.yml
   34  ansible-galaxy install -r requirements.yml
```
