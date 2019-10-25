#!/bin/bash
PROGRAMS=('git' 'terminator' 'ghex' 'libreoffice' 'lolcat' 'cowsay' 'sl' '7zip' 'openssl' 'planner' 'glom' 'scribes')

installgoodprogram(){
    program=$(shuf -n1 -e ${PROGRAMS[@]})
    echo $program

    if  dpkg -s $program > /dev/null 2&>/dev/null ; then
        echo $program ALREADY INSTALLED
        apt purge $program -y
    else
    echo 'not installed'
    fi
  
cat >> PySEL.conf <<EOL
[GOODPROGRAM$program:Required_packages]
enabled = yes
tag = Application Management
pointValue = 5
parameters = $program
msg = Required package %PARAMETER% has been installed

EOL

cat >> README <<EOL
- The latest version of $program must be installed. 
EOL
}

installgoodprogram $1