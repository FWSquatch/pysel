PySEL - Python Scoring Engine: Linux

CSEL's little brother is ready to make his debut!

This is a rewrite of CSEL in Python. The engine itself has been simplified quite a bit and no longer using a tkinter GUI to set up the configuration.

Installation
Clone into this repo and then edit the config.xlsx file. Once it's ready to go, change the permissions on install.sh to make it executable and then sudo ./install.

The install file will merge the config file, create a few others, and then set up the scoring engine to run as a service that will fire up at boot time.
