# jenkins via vagrant of virtualbox

## install vagrant on apple

```bash
> brew cask install vagrant
# check
> vagrant version
```

## install jenkins in docker container of virtualbox

```bash
# change to the directory with the Vagrantfile and
# during a while
> vagrant up
# check with login inside vagrant box
> vagrant ssh
# exit with exit
vagrant@contrib-stretch:~$ exit
# vagrant stop
> vagrant stop
# vagrant delete box
> vagrant delete
# vagrant status
> vagrant status
# validate Vagrantfile
> vagrant validate
```

## install jenkins as docker container inside vagrant box

```bash
# login inside vagrant box
> vagrant ssh
# mkdir share for jenkins data
> mkdir jenkins_home
# start docker container with lts version form docker hub
> docker run -d -p 8080:8080 -p 50000:50000 -v $PWD/jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts
# check container is running (weak test)
> docker ps
# get ip from your bridge interface eth1 config inside the Vagrantfile (ip is depends of your DHCP net range/mask)
> ip addr show eth1 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1
# Next Step
# used a webbrowser and open <IP ADDRESS FROM LAST STEP>:8080
# jenkins should start and ask for the initialAdminPassword
# Next Step
# gather initialAdminPassword from docker container
> docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword


## auto setup jenkins
https://www.codeproject.com/Articles/1056410/Setup-Configure-Jenkins-For-Your-Team-in-Automated



```

## docker housekeeping

```bash
> docker stop $(docker ps -a -q)
> docker rm $(docker ps -a -q)
```

sudo chown -Rv _apt:root /var/cache/apt/archives/partial/
sudo chmod -Rv 700 /var/cache/apt/archives/partial/


VBoxManage internalcommands sethduuid mydisk.vmdkcd



## troubleshooting

```bash
touch: cannot touch ‘/var/jenkins_home/copy_reference_file.log’: Permission denied
```

- see here the last entry from [Vice](https://stackoverflow.com/questions/44065827/jenkins-wrong-volume-permissions)

```txt
As haschibaschi stated your user in the container has different userid:groupid than the user on the host.
```


##
https://github.com/jenkinsci/docker/issues/177

git clone https://github.com/jenkinsci/docker.git jenkinsci-docker
cd jenkinsci-docker;
docker build -t jenkins-test .;
docker rm -f photobox-base-jenkins > /dev/null 2>&1;
docker run -it \
  --env JAVA_OPTS="${JAVA_OPTS}" \
  --env JENKINS_SLAVE_AGENT_PORT=50001 \
  --name photobox-base-jenkins \
  -p 8080:8080 \
  -p 50001:50001 \
  -v `pwd`/data:/var/jenkins_home \
  jenkins-test

