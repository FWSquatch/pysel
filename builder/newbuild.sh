#!/bin/bash

PKG_OK=$(dpkg-query -W --showformat='${Status}\n' rig | grep "install ok installed")
echo Checking for somelib: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No somelib. Setting up somelib."
  sudo apt-get --force-yes --yes install rig
fi

rndUser () {
USER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
echo $USER
#sudo useradd -m -u $1 $USER
#sudo adduser $USER $2
}

rndUser 1