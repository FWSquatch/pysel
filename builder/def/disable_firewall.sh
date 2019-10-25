#!/bin/bash
FUNCTIONS=("uninstall" "disable")

uninstall () ## Uninstall ufw
{
echo Firewall ufw being uninstalled...
apt purge ufw -y
}

disable ()  ## Disable ufw
{
echo Firewall ufw being disabled...
ufw disable
}

$(shuf -n1 -e "${FUNCTIONS[@]}") ## Choose a random FUNCTION

cat >> PySEL.conf <<EOL
[FIREWALL:Check_firewall]
enabled = yes
tag = Defensive Countermeasures
pointValue = 5
parameters = null
msg = Firewall has been enabled

EOL

cat >> README <<EOL
Ufw is the only firewall authorized for this machine.
EOL
