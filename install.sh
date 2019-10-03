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

defaultlocation='/home/'$(id -nu 1000)'/Desktop/score.html'
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
#mv dist /usr/local/bin/
cp -R dist /usr/local/bin/

#echo -e 'DONE\nCopying score.py and notify.sh'
#mv score.py /usr/local/bin/scoreservice
#chmod 755 /usr/local/bin/scoreservice
cp notify.sh /usr/local/bin/notify.sh
chmod 755 /usr/local/bin/notify.sh

echo -e 'DONE\nCreating /cyberpatriot directory'
mkdir -p /cyberpatriot
cp *.png /cyberpatriot/
cp *.wav /cyberpatriot/

echo -e 'DONE\nCreating Team ID Changer'
#chown $(id -nu 1000):$(id -nu 1000) SetTeam.desktop
cp SetTeam.desktop '/home/'$(id -nu 1000)'/Desktop/'
chmod 777 '/home/'$(id -nu 1000)'/Desktop/SetTeam.desktop'
cp setid.sh /cyberpatriot/
chmod +x /cyberpatriot/setid.sh
chmod 777 /usr/local/bin/

echo -e 'DONE\nRegistering scoring service'
cp pysel_scoring.service /etc/systemd/system/
systemctl enable pysel_scoring.service
systemctl start pysel_scoring.service

