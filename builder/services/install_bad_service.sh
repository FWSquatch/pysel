#!/bin/bash
SERVICES=('mosquitto' 'nginx' 'lighttpd' 'mldonkey-server' 'ejabberd' 'bind9' 'mumble-server' 'yaws' )
installbadservice(){
    service=$(shuf -n1 -e ${SERVICES[@]})
    echo $service

    if  dpkg -s $service > /dev/null 2&>/dev/null ; then
    echo $service 'installed!'

    else
    echo $service 'not installed'
    apt install $service -y
    fi
  
cat >> PySEL.conf <<EOL
[BADSERVICE$service:Prohibited_services]
enabled = yes
tag = Service Auditing
pointValue = 5
parameters = $service
msg = Prohibited service %PARAMETER% has been stopped/removed

EOL

}

installbadservice $1
