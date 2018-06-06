import yaml
print ("version of yaml ==> " + yaml.__version__)


class YamlReadConfig:
    default_config = 'default'

    def __init__(self):
        self.data = []

    def getConfigValue(self, kez):
        # Attention the config file is the package
        f = open('./configs/localhost_config.yml')
        try:
            doc = yaml.load(f)
        except yaml.YAMLError as exc:
            if hasattr(exc, 'problem_mark'):
                mark = exc.problem_mark
                print ("Error position: (%s:%s)" %
                       (mark.line+1, mark.column+1))
        f.close()
        return_kez = doc[self.default_config][kez]
        return return_kez


# x = YamlReadConfig()

# server = x.getConfigValue('server')

# print (server)
