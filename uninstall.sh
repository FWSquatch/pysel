#!/bin/bash

rm -rf /usr/local/bin/*
pip3 uninstall pyarmor -y
systemctl stop pysel_scoring_service