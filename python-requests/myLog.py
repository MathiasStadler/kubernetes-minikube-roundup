# from here
# http://docs.python-guide.org/en/latest/writing/logging/
# OLD import logging
# OLD logging.getLogger(__name__).addHandler(logging.NullHandler())

import os
import logging
import sys
from logging.config import fileConfig
fileConfig('./logging_config.ini', disable_existing_loggers=False)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug('Logging start')
