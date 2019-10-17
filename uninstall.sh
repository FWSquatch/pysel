#!/bin/bash

rm -rf /usr/local/bin/*
pip3 uninstall pyarmor -y


if [ $(lsb_release -r | cut -f 2) == "16.04" ] ; then
  echo 'Ubuntu 16.04 - Using systemd'
  systemctl stop pysel_scoring_service
else
  echo 'Ubuntu 14.04 - Using upstart\n SORRY FOR THE DELAY!'
  service pysel_scoring stop
fi