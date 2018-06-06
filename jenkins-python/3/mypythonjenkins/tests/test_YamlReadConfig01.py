# -*- coding: utf-8 -*-

import pytest
# from bin.YamlReadConfig import *
from .context import pythonJenkins
import os
import inspect


class TestClass01:

    def whereWeAre(self):
        print("File => %s" % os.path.basename(__file__))
        print("CLass => %s" % self.__class__.__name__)
        print ("def => %s" % inspect.stack()[1][3])

    def test_case01(self):
        self.whereWeAre()
        assert pythonJenkins.YamlReadConfig.getConfigValue(
            self, 'server') == 'localhost'

    def test_case02(self):
        self.whereWeAre()
        assert getConfigValue('user') == 'admin'
