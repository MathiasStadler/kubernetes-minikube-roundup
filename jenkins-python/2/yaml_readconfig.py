import yaml

f = open('jenkins_python_cfg.yml')

dataMap = yaml.load(f)

f.close()


print ""
print "=-----------="
print "dataMap is a ", type(dataMap), dataMap
print "=-----------="
print "main items are", type(dataMap[0]), dataMap[0]

print dataMap[0]

a = dataMap[0]

print type(a)

print a.get('user')
print a['user']

user = a['user']

print user
