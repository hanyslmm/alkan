#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

import webbrowser
import time
print("this program started on "+time.ctime())

total_logicallink = input("how many logicallink you need ")
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
    text('name=Obour_access_SS25_pool1')
    text('\n')

# set linkset
with tag('linkset'):
    text('\n')
    text('name=SS25_Access_2G-BSC_2040')
    text('\n')
    text('protocol=InetSigTran')
    text('\n')
    text('linksettype="Linkset SS7/SCTP"')
    text('\n')
    text('node1name=SS25_Pool_2G')
    text('\n')
    text('node2name=BSC_2040')
    text('\n')

# SET sigtranlink tag for MGWS1
while(counter < total_logicallink):
    if counter < 10:
        with tag('sigtranlink'):
            text('\n')
            text('name=SS25_MGWS1_0{}-MGWS1_SS25_0{}_'.format(counter\
                                                                    , counter))
            text('\n')
            text('linksetname=SS25_Access_2G-BSC_2040')
            text('\n')
            text('associationname=SS25_MGWS1_0{}-MGWS1_SS25_0{}'.format(counter\
                                                                    , counter))
            text('\n')
    else:
        with tag('sigtranlink'):
            text('\n')
            text('name=SS25_MGWS1_{}-MGWS1_SS25_{}_'.format(counter, counter))
            text('\n')
            text('linksetname=SS25_Access_2G-BSC_2040')
            text('\n')
            text('associationname=SS25_MGWS1_{}-MGWS1_SS25_{}'.format(counter\
                                                                    , counter))
            text('\n')

    counter += 1
counter = 00
# SET sigtranlink tag for MGWR1
while(counter < total_logicallink):
    if counter < 10:
        with tag('sigtranlink'):
            text('\n')
            text('name=SS25_MGWR1_0{}-MGWR1_SS25_0{}_'.format(counter\
                                                                , counter))
            text('\n')
            text('linksetname=SS25_Access_2G-BSC_2040')
            text('\n')
            text('associationname=SS25_MGWR1_0{}-MGWR1_SS25_0{}'.format(counter\
                                                                    , counter))
            text('\n')
    else:
        with tag('sigtranlink'):
            text('\n')
            text('name=SS25_MGWR1_{}-MGWR1_SS25_{}_'.format(counter
                                                                    , counter))
            text('\n')
            text('linksetname=SS25_Access_2G-BSC_2040')
            text('\n')
            text('associationname=SS25_MGWR1_{}-MGWR1_SS25_{}'.format(counter
                                                                    , counter))
            text('\n')

    counter += 1

result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline = '\r\n'
)


file = open("SS25_BSC2040.txt", "w")
file.write(result)
file.close()

print ('done')
