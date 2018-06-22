#!/bin/bash

set -e

LATEST_VIRTUAL_BOX_VERSION_FILE="/tmp/latestVirtuboxVersion.txt"
curl https://download.virtualbox.org/virtualbox/LATEST.TXT -o ${LATEST_VIRTUAL_BOX_VERSION_FILE}
cat ${LATEST_VIRTUAL_BOX_VERSION_FILE}

# from here
# https://stackoverflow.com/questions/18780322/listing-files-with-curl
# sed string from here
# https://stackoverflow.com/questions/21264626/how-to-strip-out-all-of-the-links-of-an-html-file-in-bash-or-grep-or-batch-and-s

LATEST_VIRTUAL_BOX_DMG_NAME=$(curl -s http://download.virtualbox.org/virtualbox/$(cat ${LATEST_VIRTUAL_BOX_VERSION_FILE})/ --list-only | grep dmg | sed -n 's/.*href="\([^"]*\).*/\1/p')

curl http://download.virtualbox.org/virtualbox/$(cat ${LATEST_VIRTUAL_BOX_VERSION_FILE})/${LATEST_VIRTUAL_BOX_DMG_NAME} -O

hdiutil mount ${LATEST_VIRTUAL_BOX_DMG_NAME}

sudo installer -pkg /Volumes/VirtualBox/VirtualBox.pkg -target /

hdiutil unmount /Volumes/VirtualBox/

# keep file
# rm VirtualBox-4.2.12-84980-OSX.dmg

exit 0

# delete via cli
# from here
# https://github.com/iamrToday/pkg-remove/blob/master/pkg-remove.sh

software="org.virtualbox.pkg.virtualbox"

installPath=$(pkgutil --pkg-info ${software} | grep 'location:' | awk '{print $2}')
cd /${installPath}
#start uninstall
pkgutil --only-files --files ${software} | tr '\n' '\0' | xargs -n 1 -0 rm -if
pkgutil --only-dirs --files ${software} | tr '\n' '\0' | xargs -n 1 -0 rm -ifr
sudo pkgutil --forget ${software}

exit 0

wget http://download.virtualbox.org/virtualbox/4.2.12/Oracle_VM_VirtualBox_Extension_Pack-4.2.12-84980.vbox-extpack
$ sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-4.2.12-84980.vbox-extpack
$ rm Oracle_VM_VirtualBox_Extension_Pack-4.2.12-84980.vbox-extpack

http://osxdaily.com/2014/07/31/manual-complete-app-removal-mac-os-x-terminal/
