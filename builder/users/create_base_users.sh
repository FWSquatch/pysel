#!/bin/bash

rndUser(){ 
for (( i = 0; i <= $1; i++ )); do 
    USER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
    sudo useradd -m $USER
    echo -e '1P@ssword!\n1P@ssword!' | sudo passwd $USER
    echo Creating base user: $USER
    
cat >> PySEL.conf <<EOL
[BASE$USER:Remove_users]
enabled = yes
tag = User Management
pointValue = -10
parameters = $USER
msg = Essential user %PARAMETER% has been deleted!

EOL

cat >> README <<EOL
USER - $USER
EOL
done
}

rndUser $1