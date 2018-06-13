# jenkins-python

## install

```bash
# python2
> pip install python-jenkins
# python3
> pip3 install python-jenkins
```

```bash
# python 2.x
> pip install PyYAML
# python 3
> pip3 install PyYAML
```

## sample code for [yaml](https://www.programcreek.com/python/example/10228/yaml.YAMLError)

## hints

### show tabs inside Makefile

```bash
> cat -e -t -v  Makefile
```

## sample project structure python 3 projects

```txt
http://docs.python-guide.org/en/latest/writing/structure/
```

## website with include python repl

```txt
https://www.programiz.com/python-programming/property
```

## book jenkins api

```txt
https://media.readthedocs.org/pdf/python-jenkins/latest/python-jenkins.pdf
```

## jenkinsapi vs python-jenkins

```txt
https://github.com/pycontribs/jenkinsapi
```

```python
from jenkinsapi.jenkins import Jenkins
```

## get api token

- [from here last entry](https://stackoverflow.com/questions/36633725/generate-jenkins-api-token-using-rest-api)

```bash
>brew install HTML-XML-utils
> curl --silent --basic http://<username>:<password>@<jenkins-url>:<port>/me/configure | hxselect '#apiToken' | sed 's/.*value="\([^"]*\)".*/\1\n/g'
> curl --silent --basic http://admin:admin@192.168.178.48:8080/me/configure | hxselect '#apiToken' | sed 's/.*value="\([^"]*\)".*/\1\n/g'
b74f5c5f16165987db62782814cfaa10n
```

## api in swagger yaml

```txt
https://github.com/cliffano/swaggy-jenkins/blob/master/spec/jenkins-api.yml
```

## plugins via curl

```txt
curl -s -k "https://$jenkins/pluginManager/api/json?pretty=1&tree=plugins\[shortName,longName,version\]"
```

## system properties

```txt
https://stackoverflow.com/questions/37035319/as-a-jenkins-administrator-how-do-i-get-a-users-api-token-without-logging-in-a
```
