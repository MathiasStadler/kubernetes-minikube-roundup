import yaml
print ("version of yaml ==> " + yaml.__version__)

default_config = 'default'


def get_cfg(kez):
    f = open('../jenkins_python_cfg2.yml')
    try:
        doc = yaml.load(f)
    except yaml.YAMLError as exc:
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            print ("Error position: (%s:%s)" % (mark.line+1, mark.column+1))
    f.close()

    print (type(doc))
    print (type(doc[default_config]))
    print(doc[default_config]['user'])
    server = doc[default_config]['server']
    print(server)
    return "rr"


print get_cfg("server")
