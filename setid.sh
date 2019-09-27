#!/bin/bash

echo "Enter the Team ID provided by your coach"
read teamID

echo $teamID > /usr/local/bin/TEAM
rm -rf '/home/'$(id -nu 1000)'/Desktop/SetTeam.desktop'

