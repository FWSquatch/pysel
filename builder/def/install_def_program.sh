#!/bin/bash
PROGRAMS=('clamav' 'rkhunter' 'chkrootkit' 'lynis')

installgoodprogram(){
    program=$(shuf -n1 -e ${PROGRAMS[@]})
    echo $program

    if  dpkg -s $program > /dev/null 2&>/dev/null ; then
        echo $program ALREADY INSTALLED
    else
    echo 'not installed'
    fi
  
cat >> PySEL.conf <<EOL
[GOODPROGRAM$program:Required_packages]
enabled = yes
tag = Defensive Countermeasures
pointValue = 5
parameters = $program
msg = Beneficial package %PARAMETER% has been installed

EOL
}

installgoodprogram $1