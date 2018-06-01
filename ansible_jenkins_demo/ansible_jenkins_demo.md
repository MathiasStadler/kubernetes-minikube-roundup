# ansible_jenkins_demo

## ansible-jenkins-role github [here](https://github.com/geerlingguy/ansible-role-jenkins)

## set environment variables

```bash
> . ./init.sh
```

## install requirements roles

```bash
> ansible-galaxy install -r requirements.yml
```

## first easy playbook.yml

```yaml
- hosts: all
  vars:
    jenkins_hostname: jenkins.example.com
  roles:
    - role: geerlingguy.java
    - role: geerlingguy.jenkins
      become: true
```

## syntax check

```bash
> ansible-playbook --syntax-check playbook.yml
```

## run playbook

```bash
> ansible-playbook playbook.yml
```

DASH name: Install Jenkins and its plugins
hosts: jenkins_servers
remote_user: root

vars:
jenkins_hostname: localhost
jenkins_plugins: - git - sonar - ssh - gerrit-trigger - gearman-plugin - zmq-event-publisher - ansicolor - matrix-project - workflow-aggregator - extended-read-permission - ssh-slaves

roles:
DASH geerlingguy.jenkins

https://github.com/geerlingguy/ansible-role-jenkins/issues/164

https://github.com/geerlingguy/ansible-role-jenkins/issues/129
