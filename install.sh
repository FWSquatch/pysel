#!/bin/bash

echo -e 'Checking for Dependencies:'

for package in python3-pip; do
    if dpkg -s $package > /dev/null 2>/dev/null; then
        echo $package is installed
        else
        echo -e "$package is NOT installed!"
        apt install $package
    fi
done

echo -e 'DONE\nInstalling Python modules'
for module in xlrd pyarmor; do
    pip3 install $module
done

defaultuser=$(getent passwd 1000 | cut -d: -f 1)
echo -e "The default user is currently set to" $defaultuser
echo -e "Press [enter] to keep this user or enter a new default user:"
read cpuser
if [ -z "$cpuser" ] ; then
    cpuser=$defaultuser
else :    
fi

defaultlocation='/home/'$cpuser'/Desktop/score.html'
echo -e "The score report location is currently set to "$defaultlocation
echo -e 'Press [enter] to keep it there or enter a new location:'
read scorelocation
if [ -z "$scorelocation" ] ; then
    echo -e '#!usr/bin/env python3\n\nSCORE_REPORT_LOCATION = '\"$defaultlocation\" > score.py
else
    echo -e '#!usr/bin/env python3\n\nSCORE_REPORT_LOCATION = '\"$scorelocation\" > score.py
fi

echo -e 'DONE\nReading configuration file'
python3 readconfig.py config.xlsx

echo -e 'DONE\nCreating scoring engine'
cat pysel.py >> score.py 

echo -e 'DONE\nObfuscating scoring engine'
sudo pyarmor obfuscate score.py
cp -R dist /usr/local/bin/

echo -e 'DONE\nCopying score.py and notify.sh'
cp notify.sh /usr/local/bin/notify.sh
chmod 755 /usr/local/bin/notify.sh

echo -e 'DONE\nCreating /cyberpatriot directory'
mkdir -p /cyberpatriot
cp *.png /cyberpatriot/
cp *.wav /cyberpatriot/

echo -e 'DONE\nCreating Team ID Changer'
chown $cpuser:$cpuser SetTeam.desktop
cp SetTeam.desktop '/home/'$cpuser'/Desktop/'
chmod 777 '/home/'$cpuser'/Desktop/SetTeam.desktop'
cp setid.sh /cyberpatriot/
chmod +x /cyberpatriot/setid.sh
chmod 777 /usr/local/bin/

echo -e 'DONE\nRegistering scoring service'
if [ $(lsb_release -r | cut -f 2) == "16.04" ] ; then
  echo 'Ubuntu 16.04 - Using systemd'
  cp pysel_scoring.service /etc/systemd/system/
  systemctl enable pysel_scoring.service
  systemctl start pysel_scoring.service
else
  echo 'Ubuntu 14.04 - Using upstart'
  cp pysel_scoring.conf /etc/init/
  echo 'Pysel will fire in 30 seconds'
  service pysel_scoring start &
fi