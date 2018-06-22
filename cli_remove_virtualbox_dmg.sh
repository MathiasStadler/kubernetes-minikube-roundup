#!/bin/bash

checkProcessIsRunning() {
	# run test prozess from here
	# https://stackoverflow.com/questions/2903354/bash-script-to-check-running-process
	SERVICE=$1
	if ps ax | grep -v grep | grep -v $0 | grep $SERVICE >/dev/null; then
		echo "$SERVICE service running"
		return 0
	else
		echo "$SERVICE is not running"
		return 1
	fi
}

deleteSoftwarePackages() {

	toDeleteSotwarePackages=$1
	echo "Start deleteSoftwarePackages"

	echo "Software Packages => $1"

	installPath=$(pkgutil --pkg-info ${toDeleteSotwarePackages} | grep 'location:' | awk '{print $2}')

	echo "Install Path of Software => /${installPath}"

	cd /${installPath}

	echo "Files to deleted in directory $PWD"

	#old pkgutil --only-files --files ${toDeleteSotwarePackages}
	pkgutil --only-files --files ${toDeleteSotwarePackages} | tr '\n' '\0' | xargs -n 1 -0 ls -l
	pkgutil --only-dirs --files ${toDeleteSotwarePackages} | tr '\n' '\0' | xargs -n 1 -0 ls -l

	pkgutil --only-files --files ${toDeleteSotwarePackages} | tr '\n' '\0' | xargs -n 1 -0 rm -if
	pkgutil --only-dirs --files ${toDeleteSotwarePackages} | tr '\n' '\0' | xargs -n 1 -0 rm -ifr
	sudo pkgutil --forget ${toDeleteSotwarePackages}

	echo "Finish deleteSoftwarePackages"

}

# stop all minikube instances
# show status
ls -l ~/.minikube/machines/ | grep ^d | awk '{print $9}' | xargs -I '{}' minikube status --profile {}
# stop all instances
ls -l ~/.minikube/machines/ | grep ^d | awk '{print $9}' | xargs -I '{}' minikube delete --profile {}
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
vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate

# stop VirtualBox
# osascript -e 'quit app "VirtualBox"'

SERVICE="VirtualBox.app"

if checkProcessIsRunning $SERVICE; then

	echo "Running stop services"
	# stop VirtualBox
	osascript -e 'quit app "VirtualBox"'

else

	"Fine Service not running"
fi

# delete via cli
# from here
# https://github.com/iamrToday/pkg-remove/blob/master/pkg-remove.sh

INSTALL_VIRTUALBOX_PRODUCT_LIST="/tmp/virtualbox_product_list.txt"

pkgutil --pkgs | grep virtualbox >${INSTALL_VIRTUALBOX_PRODUCT_LIST}

# loop over file from here
# https://stackoverflow.com/questions/1521462/looping-through-the-content-of-a-file-in-bash
# while read p; do
#	echo "Software for rermove => $p"
#done <${INSTALL_VIRTUALBOX_PRODUCT_LIST}

# loop over command output as list
# from here
# https://stackoverflow.com/questions/2859908/iterating-over-each-line-of-ls-l-output

pkgutil --pkgs | grep virtualbox | while read x; do echo "hallo $x "; done

pkgutil --pkgs | grep virtualbox | while read softwarePackage; do deleteSoftwarePackages $softwarePackage; done

exit 0

software="org.virtualbox.pkg.virtualbox"

# loop over a list
# files=("/etc/passwd" "/etc/group" "/etc/hosts")
# for i in "${files[@]}"; do
#	echo "$i"
#done

exit 0

installPath=$(pkgutil --pkg-info ${software} | grep 'location:' | awk '{print $2}')

echo "Install Software Path => ${installPath}"

cd /${installPath}

echo "Files to deleted"
pkgutil --only-files --files ${software}

pkgutil --only-dirs --files ${software}

exit 0

#start uninstall
pkgutil --only-files --files ${software} | tr '\n' '\0' | xargs -n 1 -0 rm -if
pkgutil --only-dirs --files ${software} | tr '\n' '\0' | xargs -n 1 -0 rm -ifr
sudo pkgutil --forget ${software}

exit 0
