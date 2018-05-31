# jenkins via vagrant of virtualbox

## install vagrant on apple

```bash
> brew cask install vagrant
# check
> vagrant version
```

## install jenkins in docker container of virtualbox

```bash
> vagrant init minimum/ubuntu-trusty64-docker
# add vagrant up download the image and start
> vagrant up
```

## install jenkins as docker container inside vagrant box

```bash
> vagrant ssh
> docker pull jenkins/jenkins:lts
> docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
> docker run --name myjenkins -p 8080:8080 -p 50001:50001 --env JENKINS_SLAVE_AGENT_PORT=50001 jenkins/jenkins:lts
> docker run --name myjenkins -p 8080:8080 -p 50001:50001 --env JENKINS_SLAVE_AGENT_PORT=50001 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
> docker run -d -p 8080:8080 -p 50000:50000 -v $PWD/jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts
```

## docker housekeeping

```bash
> docker stop $(docker ps -a -q)
> docker rm $(docker ps -a -q)
```


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

