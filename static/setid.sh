#!/bin/bash

echo "Enter the Team ID provided by your coach"
read teamID

echo $teamID > /usr/local/bin/pysel/TEAM
rm -rf '/home/'$(getent passwd 1000 | cut -d: -f 1)'/Desktop/SetTeam.desktop'