from YamlReadConfig import YamlReadConfig
import jenkins
import sys

config = YamlReadConfig()

print (config.getConfigValue('server'))

sys.exit(0)


server = jenkins.Jenkins('http://192.168.178.48:8080',
                         username='admin', password='admin')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
