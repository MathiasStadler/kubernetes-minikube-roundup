import yaml
print ("version of yaml ==> " + yaml.__version__)

f = open('../jenkins_python_cfg.yml')

# doc = yaml.load(f)

try:
    doc = yaml.load(f)
except yaml.YAMLError as exc:
    if hasattr(exc, 'problem_mark'):
        mark = exc.problem_mark
        print ("Error position: (%s:%s)" % (mark.line+1, mark.column+1))


f.close()

print(doc[0]['user'])

server = doc[0]['server']

print(server)
