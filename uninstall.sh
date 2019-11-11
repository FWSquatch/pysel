#!/bin/bash

echo -e 'Removing /usr/local/bin/pysel directory...'

rm -rf /usr/local/bin/pysel

echo -e 'DONE\nStopping and disabling pysel_scoring.service...'
systemctl stop pysel_scoring.service
systemctl disable pysel_scoring.service

echo -e 'DONE\nRemoving scoring service from systemd...'
rm -rf /etc/systemd/system/pysel_scoring.service

echo -e 'DONE'
