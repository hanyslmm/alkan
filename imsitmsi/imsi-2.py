#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


# shokraaaaaaaaaaaaaaaan


# read csv file to create DataFrame sheet

df = pd.read_csv("first.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'first'))

# read csv file to create DataFrame sheet
df = pd.read_csv("first2.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'first2'))

# read csv file to create DataFrame sheet
df = pd.read_csv("obour.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'obour'))

# read csv file to create DataFrame sheet
df = pd.read_csv("hosary2.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'hosary2'))

# read csv file to create DataFrame sheet
df = pd.read_csv("sawah.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'sawah'))

# read csv file to create DataFrame sheet
df = pd.read_csv("smoha.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'smoha'))


# read csv file to create DataFrame sheet
df = pd.read_csv("awayed.csv", skip_blank_lines=False)
df=df.replace(" ",np.NaN)
ratio = (len(df[df['IMSI'].notnull()])/len(df))*100
print ("imsi success ratio {}% for {}".format(ratio, 'awayed'))
