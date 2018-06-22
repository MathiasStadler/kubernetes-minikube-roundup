# Motivation install virtualbox via terminal

## source

- [from here](https://slaptijack.com/system-administration/os-x-cli-install-virtualbox/)

## install

```bash
LATEST_VIRTUAL_BOX_VERSION_FILE="/tmp/latestVirtuboxVersion.txt"
curl https://download.virtualbox.org/virtualbox/LATEST.TXT -o ${LATEST_VIRTUAL_BOX_VERSION_FILE}
cat ${LATEST_VIRTUAL_BOX_VERSION_FILE}


curl http://download.virtualbox.org/virtualbox/4.2.12/VirtualBox-4.2.12-84980-OSX.dmg
```
