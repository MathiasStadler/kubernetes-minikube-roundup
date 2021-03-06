#!/bin/bash

set -e

TEMP_DIR="/tmp"

LATEST_VIRTUAL_BOX_VERSION_FILE="/tmp/latestVirtualboxVersion.txt"
curl https://download.virtualbox.org/virtualbox/LATEST.TXT -o ${LATEST_VIRTUAL_BOX_VERSION_FILE}
cat ${LATEST_VIRTUAL_BOX_VERSION_FILE}

# from here
# https://stackoverflow.com/questions/18780322/listing-files-with-curl
# sed string from here
# https://stackoverflow.com/questions/21264626/how-to-strip-out-all-of-the-links-of-an-html-file-in-bash-or-grep-or-batch-and-s

LATEST_VIRTUAL_BOX_DMG_NAME="$(curl -s http://download.virtualbox.org/virtualbox/"$(cat ${LATEST_VIRTUAL_BOX_VERSION_FILE})"/ --list-only | grep dmg | sed -n 's/.*href="\([^"]*\).*/\1/p')"

# check download file already there
if [[ -e "${TEMP_DIR}/${LATEST_VIRTUAL_BOX_VERSION_FILE}" ]]; then

	echo " Ok we used file from directory"

else

	echo "Download file"
	curl "http://download.virtualbox.org/virtualbox/$(cat ${LATEST_VIRTUAL_BOX_VERSION_FILE})/${LATEST_VIRTUAL_BOX_DMG_NAME}" -o "$TEMP_DIR/${LATEST_VIRTUAL_BOX_DMG_NAME}"

fi

echo "VirtualBox file => ${TEMP_DIR}/${LATEST_VIRTUAL_BOX_DMG_NAME}"

hdiutil mount "${TEMP_DIR}/${LATEST_VIRTUAL_BOX_DMG_NAME}"

sudo installer -pkg /Volumes/VirtualBox/VirtualBox.pkg -target /

hdiutil unmount /Volumes/VirtualBox*

exit 0
