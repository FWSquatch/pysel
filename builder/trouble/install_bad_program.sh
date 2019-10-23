#!/bin/bash
USERS=('alice' 'bob' 'charlie' 'doug' 'edward' 'fred' 'greg' 'harry' 'ivan' 'julie' 'kate' 'leonard' 'mike' 'ned' 'oscar' 'pete' 'quinn' 'rod' 'steve' 'trish' 'victor' 'william')

addfakesudo () ## Add a random bad user to sudo
{
if id -u $1 > /dev/null ; then :
else
    useradd -m $1 
    usermod -aG sudo $1  
  
cat >> PySEL.conf <<EOL
[$1:Remove_from_sudo]
enabled = yes
pointValue = 5
parameters = $user 
msg = User %PARAMETER% is no longer an administrator

EOL
fi
}

user=$(shuf -n1 -e ${USERS[@]})
while id -u $user > /dev/null; do
    echo USER: $user
    user=$(shuf -n1 -e ${USERS[@]})
    if id -u $user ; then :
    else
    break
    fi
done


addfakesudo $user

