#!/bin/bash
USERS=('alice' 'bob' 'charlie' 'doug' 'edward' 'fred' 'greg' 'harry' 'ivan' 'julie' 'kate' 'leonard' 'mike' 'ned' 'oscar' 'pete' 'quinn' 'rod' 'steve' 'trish' 'victor' 'william')

addsudouser () ## Add a random user
{
if id -u $1 > /dev/null ; then :
else
    useradd -m $1 
cat >> PySEL.conf <<EOL
[$1:Add_to_sudo]
enabled = yes
pointValue = 5
parameters = $user 
msg = User %PARAMETER% is now an administrator

EOL

cat >> README <<EOL
Authorized Admin: $user
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
addsudouser $user

