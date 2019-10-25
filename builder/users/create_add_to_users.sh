#!/bin/bash

rndUser(){ 
for (( i = 0; i <= $1; i++)); do 
    USER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
    echo Creating USER TO ADD: $USER
    
cat >> PySEL.conf <<EOL
[BASESUDO$USER:Add_users]
enabled = yes
tag = User Management
pointValue = 5
parameters = $USER
msg = User %PARAMETER% has been created

EOL

cat >> README <<EOL
USER - $USER
EOL
done
}

rndUser $1
