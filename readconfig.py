#!/usr/bin/env python3

import xlrd, sys, json

workbook = xlrd.open_workbook(sys.argv[1])
sheet = workbook.sheet_by_index(0)

masterList = []
for rowx in range(sheet.nrows):
    cols = sheet.row_values(rowx)
    if cols[0][:1] != "#":
        masterList.append(cols)
for element in masterList:
    element.append("MISS")   

stringyList = json.dumps(masterList)
payload = "\nmaster = " + stringyList + "\n\n"
f = open('score.py','a')
f.write(payload)
f.close()