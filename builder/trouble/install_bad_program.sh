#!/bin/bash
PROGRAMS=('ophcrack' 'john' 'recon-ng' 'wireshark' 'kismet' 'braa' 'ettercap-graphical' 'aircrack-ng' 'airgraph-ng' 'pompem' 'whatweb' 'wfuzz' 'websploit' 'sqlmap' 'skipfish' 'nikto' 'sugarplum' 'packit' 'reaver' 'mdk3' 'pixiewps' 'rarcrack' 'sipcrack' 'pyrit' 'pdfcrack' 'hydra' 'fcrackzip' 'thc-ipv6' 't50' 'slowhttptest' 'yersinia' 'tshark' 'tcpxtract' 'sslsplit')

installbadprogram(){
    program=$(shuf -n1 -e ${PROGRAMS[@]})
    echo $program

    if  dpkg -s $program > /dev/null 2&>/dev/null ; then
    echo 'installed!'
    else
    echo 'not installed'
    fi
  
cat >> PySEL.conf <<EOL
[BADPROGRAM$program:Remove_from_sudo]
enabled = yes
tag = Prohibited Software
pointValue = 5
parameters = $program
msg = Prohibited package %PARAMETER% has been removed

EOL
fi
}