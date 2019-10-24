#!/bin/bash

# Variables
POINTS=0
PUSER=`awk -F: '{if ($3 == 1000) print $1}' /etc/passwd`
HTML="/home/$PUSER/Desktop/Score.html"
README="/home/$PUSER/Desktop/README.html"

# Print to Score or Readme
prntScore () {
echo "$1 </br>" >> $HTML
}

prntRead() {
echo "$1 </br>" >> $README
}

# User Creating 
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' rig | grep "install ok installed")
echo Checking for somelib: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No somelib. Setting up somelib."
  sudo apt-get --force-yes --yes install rig
fi

sudoUsers () { 
for I in {1..$1}; do G=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`; sudo useradd -m $G;sudo usermod -aG sudo $G; prntRead $G; echo -e '1P@ssword!\n1P@ssword!' | sudo passwd $G; done 
}

extraUsers () { 
for I in {1..$1}; do G=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`; sudo useradd -m $G; prntRead $G; echo -e '1P@ssword!\n1P@ssword!' | sudo passwd $G; done 
}

ADDUSER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
DELUSER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
HIDDENUSER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
BADSUDO=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
BADPASS=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
CHAGEUSER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
BADROOT=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`
NOPASSUSER=`rig | awk 'NR==1{print $1}' | tr '[:upper:]' '[:lower:]'`

createUsers () {
# Create Admins
echo "<H3>Administrators</H3></br>" >> $README
sudoUsers 4
# Create Standard Users
echo "<H3>Standard Users</H3></br>" >> $README
extraUsers 1
prntRead $ADDUSER
extraUsers 2
sudo useradd -m $DELUSER
sudo useradd -r -s /bin/bash $HIDDENUSER
extraUsers 1
sudo useradd -m $BADSUDO; sudo usermod -aG sudo $BADSUDO; prntRead $BADSUDO
sudo useradd -m $BADPASS; sudo passwd -d $BADPASS; prntRead $BADPASS
sudo useradd -m $CHAGEUSER; prntRead $CHAGEUSER
sudo useradd -r -s /bin/bash $BADROOT; sudo sed -i "s/$BADROOT:x:*:/$BADROOT:x:0:/g" /etc/passwd
extraUsers 1
sudo useradd -m $NOPASSUSER; sudo usermod -aG nopasswdlogin; prntRead $NOPASSUSER
}

flaw () {
FL1=`grep $GREP $FILE`
if [[ $FL1 = *"$RESULT"* ]]; then
  echo "<tr><td>$TEXT</td><td style='text-align:center'>$PTS</td><td>$CAT</td></tr>" >> $HTML && let "POINTS=POINTS+$PTS" 
fi
}

rflaw () {
FL1=`grep $GREP $FILE`
if [[ $FL1 != *"$RESULT"* ]]; then
  echo "<tr><td>$TEXT</td><td style='text-align:center'>$PTS</td><td>$CAT</td></tr>" >> $HTML && let "POINTS=POINTS+$PTS"
fi
}

# Web Page Setup
echo "" > $HTML
echo "<html>" >> $HTML
echo "<head>" >> $HTML
echo "<meta http-equiv="refresh" content="15">" >> $HTML
echo "<style>
table, th, td {
  border: 1px solid black;
  padding: 2px;
  border-collapse: collapse;
  text-align: left;
}
table tr:nth-child(even) {
  background-color: #eee;
}
table tr:nth-child(odd) {
  background-color: #fff;
}
table th {
  color: white;
  background-color: black;
}
</style>" >> $HTML
echo "</head>" >> $HTML
echo "<body>" >> $HTML
echo "<h3>Ubuntu Practice</h3>" >> $HTML
echo '<table style="width:100%"><tr><th>Flaw</th><th>Score</th><th>Category</th></tr>' >> $HTML


############## Scoring #####################

# Flaw01 - Created user account ADDUSER
GREP="$ADDUSER"
FILE="/etc/passwd"
RESULT="$ADDUSER"
PTS="1"
TEXT="Created user account $ADDUSER"
CAT="User Auditing"
flaw
#/

# Flaw02 - Deleted user account DELUSER
GREP="$DELUSER"
FILE="/etc/passwd"
RESULT="$DELUSER"
PTS="1"
TEXT="Removed user account $DELUSER"
CAT="User Auditing"
rflaw
#/

# Flaw03 - Deleted user account HIDDENUSER
GREP="$HIDDENUSER"
FILE="/etc/passwd"
RESULT="$HIDDENUSER"
PTS="1"
TEXT="Removed user account $HIDDENUSER"
CAT="User Auditing"
rflaw
#/

# Flaw04 - $BADSUDO is no longer an administrator
GREP="$BADSUDOUSER"
FILE="/etc/group"
RESULT="$BADSUDO"
PTS="1"
TEXT="$BADSUDO is no longer an administrator"
CAT="User Auditing"
rflaw
#/

# Flaw05 - Changed insecure password for user $BADPASS
GREP="$BADPASS"
FILE="/etc/shadow"
RESULT="$BADPASS:$"
PTS="1"
TEXT="Changed insecure password for user $BADPASS"
CAT="User Auditing"
flaw
#/

# Flaw06 - $CHAGEUSER now has a maximum password age
GREP="$CHAGEUSER"
FILE="/etc/shadow"
RESULT="99999"
PTS="1"
TEXT="$CHAGEUSER now has a maximum password age"
CAT="User Auditing"
rflaw
#/

# Flaw07 - Deleted user account $BADROOT
GREP="$BADROOT"
FILE="/etc/passwd"
RESULT="$BADROOT"
PTS="1"
TEXT="Removed user account $BADROOT"
CAT="User Auditing"
rflaw
#/

# Flaw08 - $NOPASSUSER can no longer login without a password
GREP="nopasswdlogin"
FILE="/etc/group"
RESULT="$NOPASSUSER"
PTS="1"
TEXT="$NOPASSUSER can no longer login without a password"
CAT="User Auditing"
rflaw
#/

# Flaw09 - Guest account is disabled
GREP="allow-guest"
FILE="/etc/lightdm/lightdm.conf"
RESULT="false"
PTS="2"
TEXT="Guest account is disabled"
CAT="User Auditing"
flaw 
#/



# Total Score
prntScore "<tr><td style='border: 2px solid black;'>Total points: </td><td style='border: 2px solid black;text-align:center;'>$POINTS</td></table></tr><br>"
prntScore "Last Update: `date +%T`"

# Web Page Closing
prntScore "</body></html>"
