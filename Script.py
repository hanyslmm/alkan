#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

import webbrowser
import time
print("this program started on "+time.ctime())

total_logicallink = input("how many logicallink you need: ")
map_name = input("enter mapinfo name: ")
ss_name = input("enter soft switch name on map: ")
bsc_name = input("enter BSC name on map: ")
mgw1 = input("enter first MGW name: ")
mgw2 = input("enter second MGW name: ")
ss = input("enter ss number: ")
linkset_name = "{}_{}".format(map_name, bsc_name)
counter = 00
total_logicallink = int(total_logicallink)

# first tag in script version
with tag('ss7import'):
    text('\n')
    text('version=1')
    text('\n')

# set map name mapinfo tag
with tag('mapinfo'):
    text('\n')
    text('name={}'.format(map_name))
    text('\n')

# set linkset
with tag('linkset'):
    text('\n')
    text('name={}'.format(linkset_name))
    text('\n')
    text('protocol=InetSigTran')
    text('\n')
    text('linksettype="Linkset SS7/SCTP"')
    text('\n')
    text('node1name={}'.format(ss_name))
    text('\n')
    text('node2name={}'.format(bsc_name))
    text('\n')

# SET sigtranlink tag for MGW1
while(counter < total_logicallink):
    if counter < 10:
        with tag('sigtranlink'):
            text('\n')
            text('name={}_{}_0{}-{}_{}_0{}-{}'.format(ss, mgw1, counter, mgw1\
                                                        ,ss , counter, bsc_name))
            text('\n')
            text('linksetname={}'.format(linkset_name))
            text('\n')
            text('associationname={}_{}_0{}-{}_{}_0{}'.format(ss, mgw1, counter\
                                                                , mgw1, ss, counter))
            text('\n')
    else:
        with tag('sigtranlink'):
            text('\n')
            text('name={}_{}_{}-{}_{}_{}-{}'.format(ss, mgw1, counter, mgw1\
                                                        , ss, counter, bsc_name))
            text('\n')
            text('linksetname={}'.format(linkset_name))
            text('\n')
            text('associationname={}_{}_{}-{}_{}_{}'.format(ss, mgw1, counter\
                                                                , mgw1, ss, counter))
            text('\n')

    counter += 1

counter = 00
# SET sigtranlink tag for MGW2
while(counter < total_logicallink):
    if counter < 10:
        with tag('sigtranlink'):
            text('\n')
            text('name={}_{}_0{}-{}_{}_0{}-{}'.format(ss, mgw2, counter, mgw2\
                                                                    ,ss , counter, bsc_name))
            text('\n')
            text('linksetname={}'.format(linkset_name))
            text('\n')
            text('associationname={}_{}_0{}-{}_{}_0{}'.format(ss, mgw2, counter\
                                                                , mgw2, ss, counter))
            text('\n')
    else:
        with tag('sigtranlink'):
            text('\n')
            text('name={}_{}_{}-{}_{}_{}-{}'.format(ss, mgw2, counter, mgw2\
                                                                    , ss, counter, bsc_name))
            text('\n')
            text('linksetname={}'.format(linkset_name))
            text('\n')
            text('associationname={}_{}_{}-{}_{}_{}'.format(ss, mgw2, counter\
                                                                , mgw2, ss, counter))
            text('\n')

    counter += 1

result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline = '\r\n'
)

file_txt = input("enter text file name: ")
file = open("{}.txt".format(file_txt), "w")
file.write(result)
file.close()

print ('done')
