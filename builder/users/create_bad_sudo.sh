#!/bin/bash

rndUser(){ 
#for (( i = 0; i < $1; i++ )); do 
for i in {1..$1} ; do 
    USER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
    sudo useradd -m $USER
    echo -e '1P@ssword!\n1P@ssword!' | sudo passwd $USER
    sudo usermod -aG sudo $USER
    echo Creating FAKE sudo user: $USER
    
cat >> PySEL.conf <<EOL
[FAKESUDO$USER:Remove_from_sudo]
enabled = yes
tag = User Management
pointValue = 5
parameters = $USER
msg = User %PARAMETER% is no longer an administrator

EOL

cat >> README <<EOL
USER - $USER
EOL
done
}

rndUser $1
