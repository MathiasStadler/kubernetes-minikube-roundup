# ansible command

## [slurp](http://docs.ansible.com/ansible/latest/modules/slurp_module.html) - Slurps a file from remote nodes

* copy this file to memory

```yaml
- name: Find out what the remote machine's mounts are
  slurp:
    src: /proc/mounts
  register: mounts

- debug:
    msg: "{{ mounts['content'] | b64decode }}"
```

## [set_fact](http://docs.ansible.com/ansible/latest/modules/set_fact_module.html?highlight=set_fact) - Set host facts from a task

* This module allows setting new variables. Variables are set on a host-by-host basis just like facts discovered by the setup module.
* These variables will be available to subsequent plays during an ansible-playbook run, but will not be saved across executions even if you use a fact cache.

```yaml
 Example setting host facts using key=value pairs, note that this always creates strings or booleans
- set_fact: one_fact="something" other_fact="{{ local_var }}"

# Example setting host facts using complex arguments
- set_fact:
     one_fact: something
     other_fact: "{{ local_var * 2 }}"
     another_fact: "{{ some_registered_var.results | map(attribute='ansible_facts.some_fact') | list }}"

# Example setting facts so that they will be persisted in the fact cache
- set_fact:
    one_fact: something
    other_fact: "{{ local_var * 2 }}"
    cacheable: true
```

## [file](http://docs.ansible.com/ansible/latest/modules/file_module.html) - Sets attributes of files

* Sets attributes of files, symlinks, and directories, or removes files/symlinks/directories. Many other modules support the same options as the file module - including copy, template, and assemble.

```yaml
- name: Create update directory
  file:
    path: "{{ jenkins_home }}/updates"
    # If directory, all intermediate subdirectories will be created if they do not exist. Since Ansible 1.7 they will be created with the supplied permissions.
    state: directory
    owner: jenkins
    group: jenkins
```

## [get_url](http://docs.ansible.com/ansible/latest/modules/get_url_module.html?highlight=get_url) - Downloads files from HTTP, HTTPS, or FTP to node

* Downloads files from HTTP, HTTPS, or FTP to the remote server. The remote server must have direct access to the remote resource.
* By default, if an environment variable <protocol>\_proxy is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see setting the environment), or by using the use_proxy option.
* HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.
* From Ansible 2.4 when run with –check, it will do a HEAD request to validate the URL but will not download the entire file or verify it against hashes.

```yaml
- name: Download current plugin updates from Jenkins update site
  get_url:
    url: http://updates.jenkins-ci.org/update-center.json
    dest: "{{ jenkins_home}}/updates/default.json"
    owner: jenkins
    group: jenkins
    mode: 0440
```

## [replace](http://docs.ansible.com/ansible/latest/modules/replace_module.html?highlight=replace) - Replace all instances of a particular string in a file using a back-referenced regular expression.

* This module will replace all instances of a pattern within a file.
* It is up to the user to maintain idempotence by ensuring that the same pattern would never match any replacements made.

```yaml
- name: Remove first and last line from json file
  replace:
    path: "{{ jenkins_home }}/updates/default.json"
    regexp: "1d;$d"
```

## [jenkins_plugin](http://docs.ansible.com/ansible/latest/modules/jenkins_plugin_module.html#status) - Add or remove Jenkins plugin

* Ansible module which helps to manage Jenkins plugins.

### Notes

* Plugin installation should be run under root or the same user which owns the plugin files on the disk. Only if the plugin is not installed yet and no version is specified, the API installation is performed which requires only the Web UI credentials.
* It’s necessary to notify the handler or call the service module to restart the Jenkins service after a new plugin was installed.
* Pinning works only if the plugin is installed and Jenkis service was successfully restarted after the plugin installation.
* It is not possible to run the module remotely by changing the url parameter to point to the Jenkins server. The module must be used on the host where Jenkins runs as it needs direct access to the plugin files.
* The params option was removed in Ansible 2.5 due to circumventing Ansible’s option handling

```yaml
 name: Install Jenkins plugins using password.
  jenkins_plugin:
    name: "{{ item }}"
    jenkins_home: "{{ jenkins_home }}"
    url_username: "{{ jenkins_admin_username }}"
    url_password: "{{ jenkins_admin_password }}"
    state: "{{ jenkins_plugins_state }}"
    timeout: "{{ jenkins_plugin_timeout }}"
    updates_expiration: "{{ jenkins_plugin_updates_expiration }}"
    url: "http://{{ jenkins_hostname }}:{{ jenkins_http_port }}{{ jenkins_url_prefix }}"
    with_dependencies: "{{ jenkins_plugins_install_dependencies }}"
  with_items: "{{ jenkins_plugins }}"
  when: jenkins_admin_password != ""
  notify: restart jenkins

- name: Install Jenkins plugins using token.
  jenkins_plugin:
    name: "{{ item }}"
    url_token: "{{ jenkins_admin_token }}"
    updates_expiration: "{{ jenkins_plugin_updates_expiration }}"
    url: "http://{{ jenkins_hostname }}:{{ jenkins_http_port }}{{ jenkins_url_prefix }}"
    with_dependencies: "{{ jenkins_plugins_install_dependencies }}"
  with_items: "{{ jenkins_plugins }}"
  when: jenkins_admin_token != ""
  notify: restart jenkins
```

## [jenkins_job](http://docs.ansible.com/ansible/latest/modules/jenkins_job_module.html?highlight=jenkins) - Manage jenkins jobs

### Synopsis

* Manage Jenkins jobs by using Jenkins REST API.

### Requirements

* The below requirements are needed on the host that executes this module.

  * python-jenkins >= 0.4.12
  * lxml >= 3.3.3

```yaml
# Create a jenkins job using basic authentication
- jenkins_job:
    config: "{{ lookup('file', 'templates/test.xml') }}"
    name: test
    password: admin
    url: http://localhost:8080
    user: admin

# Create a jenkins job using the token
- jenkins_job:
    config: "{{ lookup('template', 'templates/test.xml.j2') }}"
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    url: http://localhost:8080
    user: admin

# Delete a jenkins job using basic authentication
- jenkins_job:
    name: test
    password: admin
    state: absent
    url: http://localhost:8080
    user: admin

# Delete a jenkins job using the token
- jenkins_job:
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    state: absent
    url: http://localhost:8080
    user: admin

# Disable a jenkins job using basic authentication
- jenkins_job:
    name: test
    password: admin
    enabled: False
    url: http://localhost:8080
    user: admin

# Disable a jenkins job using the token
- jenkins_job:
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    enabled: False
    url: http://localhost:8080
    user: admin
```

https://stackoverflow.com/questions/44677868/failing-to-create-a-jenkins-job-via-ansible-with-jenkins-job-on-ubuntu-16-04-lts

https://github.com/ansible/ansible/blob/b89cb956092e6f28d16010dc887ee2dc46e7855b/test/integration/roles/test_jenkins_job/templates/config.xml.j2

@QUESTION which python version 2 or 3
sudo apt-get install python-jenkins
sudo apt-get install python2-lxml
