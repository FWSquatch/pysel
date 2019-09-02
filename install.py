#!/usr/bin/env python3

import csv

cfgList = []
with open('/home/jdavis/Desktop/Config.csv') as in_file:
    for row in csv.reader(in_file):
        if any(row):
            if row[0] == "#Vulnerability":
                pass
            else:
                cfgList.append(row)

f = open('pysel.cfg','w')
for line in cfgList:
    fakestring = ''
    for element in line:
        fakestring = fakestring + element + ','
    fakestring+= 'MISS\n'
    print(fakestring)
    f.write(fakestring)
f.close()
