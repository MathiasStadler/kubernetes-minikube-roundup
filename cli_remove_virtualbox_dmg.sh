#!/bin/bash

checkProcessIsRunning() {
	# run test process from here
	# https://stackoverflow.com/questions/2903354/bash-script-to-check-running-process
	SERVICE=$1
	if ps ax | grep -v grep | grep -v $0 | grep "$SERVICE" >/dev/null; then
		#old if pgrep "$SERVICE" >/dev/null; then
		echo "$SERVICE service running"
		return 0
	else
		echo "$SERVICE is not running"
		return 1
	fi
}

deleteSoftwarePackages() {

	toDeleteSoftwarePackages=$1
	echo "Start deleteSoftwarePackages"

	echo "Software Packages => $1"

	# installPath=$(pkgutil --pkg-info ${toDeleteSoftwarePackages} | grep 'location:' | awk '{print $2}')

	installPath="$(pkgutil --pkg-info ${toDeleteSoftwarePackages} | grep 'location' | awk '{$1="";print $0}' | sed -E 's/^ //g')"

	echo "Install Path of Software => /${installPath}"

	cd "/${installPath}"

	echo "Files to deleted in directory $PWD"

	#old pkgutil --only-files --files ${toDeleteSoftwarePackages}
	pkgutil --only-files --files "${toDeleteSoftwarePackages}" | tr '\n' '\0' | xargs -I '{}' -n 1 -0 ls -l "/${installPath}{}"
	pkgutil --only-dirs --files "${toDeleteSoftwarePackages}" | tr '\n' '\0' | xargs -I '{}' -n 1 -0 ls -l "/${installPath}{}"

	sudo pkgutil --only-files --files "${toDeleteSoftwarePackages}" | tr '\n' '\0' | xargs -n 1 -0 sudo rm -if
	sudo pkgutil --only-dirs --files "${toDeleteSoftwarePackages}" | tr '\n' '\0' | xargs -n 1 -0 sudo rm -ifr

	sudo pkgutil --forget "${toDeleteSoftwarePackages}"

	echo "Finish deleteSoftwarePackages"

}

# stop all minikube instances
# show status
ls -l ~/.minikube/machines/ | grep ^d | awk '{print $9}' | xargs -I '{}' minikube status --profile {}
# stop all instances
ls -l ~/.minikube/machines/ | grep ^d | awk '{print $9}' | xargs -I '{}' minikube stop --profile {}
# check
if [ "$(ls -l ~/.minikube/machines/ | grep -c ^d)" -eq "0" ]; then
	echo "OK all minikube stop"
else
	echo "Error Ups check if any minikube instance running"
	exit 1
fi

# stop first all vagrant boxes iof running
# from here
# https://askubuntu.com/questions/457329/shutting-down-all-virtualbox-vagrant-vms-in-one-easy-to-use-bash-command-that
# stop only vagrant boxes on virtualbox
vagrant global-status | grep virtualbox | awk '/running/{print $1}' | xargs -I '{}' vagrant suspend {}

if [ "$(vagrant global-status | grep virtualbox | awk '/running/{print $1}' | grep -c .)" -eq "0" ]; then
	echo "OK all VAGRANT instance stop"
else
	echo "Error Ups check if any VAGRANT instance running"
	exit 1
fi

# stop all other running vms on virtualbox
# from here
# https://askubuntu.com/questions/457329/shutting-down-all-virtualbox-vagrant-vms-in-one-easy-to-use-bash-command-that
# for Apple OS i'm replace sed -r with sed -E
# TODO check vboxmanage is available
if [[ -e /usr/local/bin/vboxmanage ]]; then
	vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate
fi
# stop VirtualBox
# osascript -e 'quit app "VirtualBox"'

SERVICE="VirtualBox.app"

if checkProcessIsRunning $SERVICE; then

	echo "Running stop services"
	# stop VirtualBox
	osascript -e 'quit app "VirtualBox"'
	killall VirtualBox
	killall VBoxXPCOMIPCD
	killall VBoxSVC

else

	echo "Fine Service not running"
fi

# delete via cli
# from here
# https://github.com/iamrToday/pkg-remove/blob/master/pkg-remove.sh

# INSTALL_VIRTUALBOX_PRODUCT_LIST="/tmp/virtualbox_product_list.txt"

# pkgutil --pkgs | grep virtualbox >${INSTALL_VIRTUALBOX_PRODUCT_LIST}

# loop over file from here
# https://stackoverflow.com/questions/1521462/looping-through-the-content-of-a-file-in-bash
# while read p; do
#	echo "Software for remove => $p"
#done <${INSTALL_VIRTUALBOX_PRODUCT_LIST}

# loop over command output as list
# from here
# https://stackoverflow.com/questions/2859908/iterating-over-each-line-of-ls-l-output

pkgutil --pkgs | grep virtualbox | while read -r x; do echo "hallo $x "; done

pkgutil --pkgs | grep virtualbox | while read -r softwarePackage; do deleteSoftwarePackages "$softwarePackage"; done

# delete VirtualBox.app
if [[ -e /Applications/VirtualBox.app ]]; then
	echo "VirtualBox.app available. So we will delete now"
	sudo rm -rf /Applications/VirtualBox.app
else
	echo " VirtualBox.app not available"
fi

exit 0
