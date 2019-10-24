#!/bin/bash
FUNCTIONS=("lightdm" "lightdm.conf.d")

lightdm.conf.d () ## Create random numbered file for lightdm.conf.d
{
newconf=$((10 * (1 + RANDOM % 9)))-ubuntu.conf
echo -e '[Seat:*]' > /etc/lightdm/lightdm.conf.d/$newconf
echo -e 'allow-guest=true' >> /etc/lightdm/lightdm.conf.d/$newconf
}

lightdm ()  ## Insert into lightdm
{
echo -e '[Seat:*]' > /etc/lightdm/lightdm.conf
echo -e 'allow-guest=true' >> /etc/lightdm/lightdm.conf
}

$(shuf -n1 -e "${COMMANDS[@]}") ## Choose a random FUNCTION

cat >> PySEL.conf << EOL
[GUESTACCOUNT:Disable_guest]
enabled = yes
tag = User Management
pointValue = 5
parameters = null
msg = Guest account disabled

EOL
