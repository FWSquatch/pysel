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
[GOODPROGRAM$program:Remove_from_sudo]
enabled = yes
tag = Benificial Software
pointValue = 5
parameters = $program
msg = Prohibited package %PARAMETER% has been removed

EOL
fi
}