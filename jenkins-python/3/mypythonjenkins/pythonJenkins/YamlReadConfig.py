import sys
import os
import logging
import yaml
print("version of yaml ==> " + yaml.__version__)


class YamlReadConfig:

    current_module = sys.modules[__name__]
    moduleDirectory = current_module.__file__
    moduleRootPath = os.path.dirname(
        os.path.abspath(moduleDirectory))+os.sep+".."+os.sep

    _default_config = 'default'
    _defaultConfigFilePath = moduleRootPath + '/configs/localhost_config.yml'

    def __init__(self, configFile=None):
        if configFile is None:
            self._configFile = self._defaultConfigFilePath

            self._configFile = configFile

    @property
    def configFile(self):
        return self._configFile

    @configFile.setter
    def configFile(self, configFile):
        self._configFile = configFile
        print("Setting config of => %s " % self._configFile)

    def getConfigValue(self, kez):

        # Attention the config file is the package
        f = open(self._defaultConfigFilePath)
        try:
            doc = yaml.load(f)
        except yaml.YAMLError as exc:
            if hasattr(exc, 'problem_mark'):
                mark = exc.problem_mark
                print("Error position: (%s:%s)" %
                      (mark.line+1, mark.column+1))
        f.close()
        # return_kez = doc[self.default_config][kez]
        return_kez = doc[self._default_config][kez]
        return return_kez


# x = YamlReadConfig()

# server = x.getConfigValue('server')

# print (server)
