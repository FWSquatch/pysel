#!/bin/bash

rndUser(){ 
for (( i = 0; i < $1; i++ )); do 
    USER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
    echo Creating bad user: $USER
    
cat >> PySEL.conf <<EOL
[BADUSER$USER:Remove_users]
enabled = yes
tag = User Management
pointValue = 5
parameters = $USER
msg = User %PARAMETER% has been removed

EOL

done
}

rndUser $1