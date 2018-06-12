from pythonJenkins.YamlReadConfig import *

# from here
# http://docs.python-guide.org/en/latest/writing/logging/
# OLD import logging
# OLD logging.getLogger(__name__).addHandler(logging.NullHandler())

import os
import logging
import sys
from logging.config import fileConfig

# found the root path of module
current_module = sys.modules[__name__]
moduleDirectory = current_module.__file__
moduleRootPath = os.path.dirname(
    os.path.abspath(moduleDirectory))+os.sep+".."+os.sep

print("moduleRootPath ======>" + moduleRootPath)

_loggingConfigFile = moduleRootPath + '/config/logging_config.ini'

fileConfig(_loggingConfigFile, disable_existing_loggers=False)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug('Logging start')
