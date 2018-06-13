import logging
import requests
import json
from myLog import logger


logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
logger.debug("hallo")

# r = requests.get('https://api.github.com/events')
# r = requests.get('https://heise.de')
# r = requests.get('http://admin:admin@172.28.128.3:8080/me/configure')
# r = requests.get(
#    'http://admin:admin@172.28.128.3:8080/api/json?depth=2&pretty=true')
# r = requests.get(
# 'http://admin:admin@172.28.128.3:8080/me/api/json/?depth=2&pretty=true')
# r = requests.get(
#    'http://admin:admin@172.28.128.3:8080/me/api/json/?pretty=true')

r = requests.get(
    'http://admin:admin@172.28.128.3:8080/me/api/xml')


# r = requests.get('http://admin:admin@172.28.128.3:8080/systemInfo')


# ?tree=artifacts[*]
# r = requests.get(
#    'http://admin:admin@172.28.128.3:8080/me/api/json?tree=jenkins.security.ApiTokenProperty[*[*]]')

logger.debug(r.text)
logger.info(r.encoding)
logger.info(r.status_code)
logger.info(r.raise_for_status)
logger.debug(r.text)
logger.info(r.raw)
print(type(r.raw))

json.loads(r.text)
rDict = r.json()


# for key, value in rDict.items():
# logger.info("kez => {} :: {}".format(key, value))
