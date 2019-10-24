#!/bin/bash

rndUser(){ 
for (( i = 0; i< $1; i++)); do 
    USER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
    sudo useradd -m $USER
    echo -e '1P@ssword!\n1P@ssword!' | sudo passwd $USER
    echo Creating humble sudo user: $USER
    
cat >> PySEL.conf <<EOL
[SUDO$USER:Add_to_sudo]
enabled = yes
tag = User Management
pointValue = 5
parameters = $user 
msg = User %PARAMETER% is now an administrator

EOL

cat >> README <<EOL
ADMIN - $USER
EOL
done
}

rndUser $1