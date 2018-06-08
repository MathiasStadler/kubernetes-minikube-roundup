from .context import pythonJenkins


class Test_YamlReadConfig:

    testClazz = None

    def test_case01(self):
        yamlReadConfig = pythonJenkins.YamlReadConfig()
        assert yamlReadConfig.getConfigValue('server') == 'localhost'

    def test_case_set_custopm_config(self):
        '''set custom config fiel'''
        yamlReadConfig = pythonJenkins.YamlReadConfig()
        assert yamlReadConfig is not None

        configFilePath = yamlReadConfig.configFile
        defaultConfigFilePath = yamlReadConfig._defaultConfigFilePath

        # assert configFilePath == defaultConfigFilePath
        # yamlReadConfig.configFile("./custom_jenkins.yml")
