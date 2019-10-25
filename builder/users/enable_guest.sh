#!/bin/bash
FUNCTIONS=("lightdm" "lightdm.conf.d" "lightdm.sneaky" "lightdm.conf.d.sneaky")

lightdm.conf.d () ## Create random numbered file for lightdm.conf.d
{
newconf=$((10 * (1 + RANDOM % 9)))-ubuntu.conf
echo $newconf being created...
mkdir -p /etc/lightdm/lightdm.conf.d
echo -e '[Seat:*]' > /etc/lightdm/lightdm.conf.d/$newconf
echo -e 'allow-guest=true' >> /etc/lightdm/lightdm.conf.d/$newconf
}

lightdm.conf.d.sneaky () ## Create random numbered file for lightdm.conf.d
{
newconf=$((10 * (1 + RANDOM % 9)))-ubuntu.conf
echo $newconf being created with extra lines ---SNEAKY---
echo -e '[Seat:*]' > /etc/lightdm/lightdm.conf.d/$newconf
echo -e 'allow-guest=false\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nallow-guest=true' >> /etc/lightdm/lightdm.conf.d/$newconf
}

lightdm ()  ## Insert into lightdm
{
echo Guest enabled via /etc/lightdm/lightdm.conf
echo -e '[Seat:*]' > /etc/lightdm/lightdm.conf
echo -e 'allow-guest=true' >> /etc/lightdm/lightdm.conf
}

lightdm.sneaky ()  ## Insert deep into lightdm
{
echo Guest enabled via extra lines being added to lightdm.conf ---SNEAKY---
echo -e '[Seat:*]' > /etc/lightdm/lightdm.conf
echo -e 'allow-guest=false\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nallow-guest=true' >> /etc/lightdm/lightdm.conf
}

$(shuf -n1 -e "${FUNCTIONS[@]}") ## Choose a random FUNCTION

cat >> PySEL.conf << EOL
[GUESTACCOUNT:Disable_guest]
enabled = yes
tag = User Management
pointValue = 5
parameters = null
msg = Guest account disabled

EOL
