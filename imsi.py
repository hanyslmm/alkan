#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


# read csv file to create DataFrame sheet
sheet = pd.read_csv(r'C:\Users\hany.msalama\alkan\probeimsi.csv')

print (sheet)
booleans = []
for imsi in sheet.IMSI:
    # if isinstance(int(imsi), int):
    if pd.isnull(imsi):
        booleans.append(False)
    else:
        booleans.append(True)
length = len(booleans)
success = 0
for bool in booleans:
    if bool == True:
        success += 1

ratio = (success/length) * 100

print ("imsi success ratio {}".format(ratio))
