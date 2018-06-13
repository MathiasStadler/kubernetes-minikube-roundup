#!/bin/bash

JENKINS_SERVER='172.28.128.3'

echo ${JENKINS_SERVER}

curl --silent --basic http://admin:admin@${JENKINS_SERVER}:8080/me/configure | hxselect '#apiToken' | sed 's/.*value="\([^"]*\)".*/\1\n/g'
