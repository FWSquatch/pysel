#!/bin/bash
USERS=('alice' 'bob' 'charlie' 'doug' 'edward' 'fred' 'greg' 'harry' 'ivan' 'julie' 'kate' 'leonard' 'mike' 'ned' 'oscar' 'pete' 'quinn' 'rod' 'steve' 'trish' 'victor' 'william')

adduser () ## Add a random user
{
if id -u $1 > /dev/null ; then :
else
useradd -m $1 
cat >> PySEL.conf <<EOL
[$1:Remove_users]
enabled = yes
pointValue = -10
parameters = $user 
msg = User %PARAMETER% has been created

EOL

cat >> README <<EOL
Authorized user: $user
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

adduser $user

