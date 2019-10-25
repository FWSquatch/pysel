#!/bin/bash

## Start the README
version=$(cat /etc/issue.net | cut -d. --fields=1,2)
sed "s/#VERSION#/$version/g" static/README-head > README

## Add Application flaws
APPFUNCTIONS=( "apps/install_bad_program.sh"\
             "apps/install_required_packages.sh" )

for i in {1..2} ; do
$(shuf -n1 -e "${APPFUNCTIONS[@]}")
done

## Add Defensive Countermeasures flaws
DEFFUNCTIONS=( "def/disable_firewall.sh"\
		"def/install_def_program.sh")

for i in {1..1} ; do
$(shuf -n1 -e "${DEFFUNCTIONS[@]}")
done

## Add Bad Service
services/add_bad_service.sh

## Is rig installed?
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' rig | grep "install ok installed")
echo Checking for rig: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No somelib. Setting up somelib."
  sudo apt-get --force-yes --yes install rig
fi

## Add some users
echo -e '\n\n----- Authorized Users -----' >> README
USERFUNCTIONS=( "users/create_base_sudo.sh 1"\
            "users/create_base_users.sh 1"\
            "users/create_bad_sudo.sh 1"\
            "users/create_add_to_sudo.sh 1"\
            "users/create_bad_users.sh 1"\
            "users/create_add_to_users.sh 1"\
	    "users/enable_guest.sh" )

for i in {1..10} ; do
$(shuf -n1 -e "${USERFUNCTIONS[@]}")
done

