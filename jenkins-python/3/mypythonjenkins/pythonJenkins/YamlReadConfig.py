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
    _defaultConfigFile = moduleRootPath + '/config/localhost_config.yml'

    def __init__(self, config=None, configFile=None):

        if config is None:
            self._config = self._default_config
        else:
            self._config = config
        logging.info(" config => {}".format(self._config))

        if configFile is None:
            self._configFile = self._defaultConfigFile
        else:
            self._configFile = configFile
        logging.info(" config File => {}".format(self._configFile))

    @property
    def configFile(self):
        return self._configFile

    @configFile.setter
    def configFile(self, configFile):
        self._configFile = configFile
        print("Setting config file of => %s " % self._configFile)

    @property
    def config(self):
        return self._configFile

    @configFile.setter
    def config(self, config):
        self._config = config
        print("Setting config of => %s " % self._configFile)

    def getConfigValue(self, kez):

        # Attention the config file is the package
        f = open(self._configFile)
        try:
            doc = yaml.load(f)
        except yaml.YAMLError as exc:
            if exc.problem_mark is not None:
                mark = exc.problem_mark
                print("Error position: (%s:%s)" %
                      (mark.line+1, mark.column+1))
            else:
                print("Something went wrong while parsing yaml file")

        f.close()
        # return_kez = doc[self.default_config][kez]
        try:
            return_kez = doc[self._config][kez]
            return return_kez
        except KeyError:
            logging.error("Kez {} not available".format(kez))
            return None


# x = YamlReadConfig()

# server = x.getConfigValue('server')

# print (server)
