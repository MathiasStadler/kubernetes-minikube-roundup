import sys
import os
import logging
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), './mypythonjenkins')))
from mypythonjenkins.pythonJenkins.YamlReadConfig import YamlReadConfig
import jenkins


# logging

# create log with 'spam_application'
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(__nmae__ + '.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler(sys.stdout)
# ch.setLevel(logging.DEBUG)
ch.setLevel(logging.NOTSET)
# create formatter and add it to the handlers
# formatter = logging.Formatter(
#    '%(asctime)s - %(name)s - %(levelname)s-8s - %(message)s')
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)-8s - %(name)s - \t %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the log
log.addHandler(fh)
log.addHandler(ch)

# log.log(0, "No set Log start")
log.debug("Debug Log Start ")
log.info("Info Log start")
log.warn("Warn Log start")
log.error("Error Loh start")
log.critical("Critical Log start")


config = YamlReadConfig('remote')

name = config.getConfigValue('name')
serverName = config.getConfigValue('server')
port = config.getConfigValue('port')
protocol = config.getConfigValue('protocol')
user = config.getConfigValue('user')
password = config.getConfigValue('password')
timeout = config.getConfigValue('timeout')


log.info("name => {} ".format(name))
log.info("serverName => {} ".format(serverName))
log.info("port => {}".format(port))
log.info("protocol => {}".format(protocol))
log.info("user => {}".format(user))
log.info("password => {}".format(len(password) * 'X'))
log.info("timeout for connect the server => {}".format(timeout))


jenkinsURL = "{}://{}:{}".format(protocol, serverName, port)


log.info("URL of Jenkins server => {}".format(jenkinsURL))

try:
    log.info("Try to connect to server")
    server = jenkins.Jenkins(jenkinsURL,
                             username=user, password=password, timeout=timeout)
except TimeoutError as err:
    log.error({"message": err.message})
except EnvironmentError as err:
    # handle other errors
    log.error({"message": err.message})
finally:
    config = None


user = server.get_whoami()
version = server.get_version()

info = server.get_info()

print(type(info))

for key, value in info.items():
    # print (key, value)
    print(key)

job = info['jobs']

print("info => {}".format(info))

print("jobs => {} ".format(job))


server.jenkins_request

print('Hello %s from Jenkins %s' % (user['fullName'], version))
