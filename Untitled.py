#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

import webbrowser
import time

total_logicallink = input("how many logicallink you need ")
counter = 00
total_logicallink = int(total_logicallink)
while(counter < total_logicallink):
    if counter < 10:
        with tag('logicallink'):
            text('\n')
            text('stacktype=IP')
            text('\n')
            text('name=SS20_MGWO1_0{}-MGWO1_SS20-0{}_'.format(counter, counter))
            text('\n')
            text('assocname=SS20_MGWO1_0{}-MGWO1_SS20_0{}'.format(counter, counter))
            text('\n')
    else:
        with tag('logicallink'):
            text('\n')
            text('stacktype=IP')
            text('\n')
            text('name=SS20_MGWO1_{}-MGWO1_SS20-{}_'.format(counter, counter))
            text('\n')
            text('assocname=SS20_MGWO1_{}-MGWO1_SS20_{}'.format(counter, counter))
            text('\n')

    counter += 1


result = indent(
    doc.getvalue(),
    indentation = ' '*4,
    newline = '\r\n'
)

print (result)

"""
<gprsimport>
version=1
</gprsimport>


<mapinfo>
name=Smoha_Access_SS20&SS21
offsetx=50
offsety=75
width=1000
height=2000
</mapinfo>


<iuinterface>
iunode1=SS20_Access_3G
iunode2=RNC07
protocol=InetUMTS
intgraphdefname="Iu-CS Interface"
name=SS20_Access_3G-RNC07
stacktype=IP


<linkgroup>
interface=SS20_Access_3G-RNC07
name=SS20_RNC07


<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-00_
assocname=SS20-MGWP2-MGWP2-SS20-00
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-01_
assocname=SS20-MGWP2-MGWP2-SS20-01
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-02_
assocname=SS20-MGWP2-MGWP2-SS20-02
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-03_
assocname=SS20-MGWP2-MGWP2-SS20-03
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-04_
assocname=SS20-MGWP2-MGWP2-SS20-04
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-05_
assocname=SS20-MGWP2-MGWP2-SS20-05
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-06_
assocname=SS20-MGWP2-MGWP2-SS20-06
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-07_
assocname=SS20-MGWP2-MGWP2-SS20-07
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-08_
assocname=SS20-MGWP2-MGWP2-SS20-08
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-09_
assocname=SS20-MGWP2-MGWP2-SS20-09
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-10_
assocname=SS20-MGWP2-MGWP2-SS20-10
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-11_
assocname=SS20-MGWP2-MGWP2-SS20-11
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-12_
assocname=SS20-MGWP2-MGWP2-SS20-12
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-13_
assocname=SS20_MGWP2_13-MGWP2_SS20_13
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-14_
assocname=SS20-MGWP2-MGWP2-SS20-14
</logicallink>

<logicallink>
stacktype=IP
name=SS20-MGWP2-MGWP2-SS20-15_
assocname=SS20-MGWP2-MGWP2-SS20-15
</logicallink>





<logicallink>
stacktype=IP
name=SS20_MGWS2_00-MGWS2_SS20_00_
assocname=SS20_MGWS2_00-MGWS2_SS20_00
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_01-MGWS2_SS20_01_
assocname=SS20_MGWS2_01-MGWS2_SS20_01
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_02-MGWS2_SS20_02_
assocname=SS20_MGWS2_02-MGWS2_SS20_02
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_03-MGWS2_SS20_03_
assocname=SS20_MGWS2_03-MGWS2_SS20_03
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_04-MGWS2_SS20_04_
assocname=SS20_MGWS2_04-MGWS2_SS20_04
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_05-MGWS2_SS20_05_
assocname=SS20_MGWS2_05-MGWS2_SS20_05
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_06-MGWS2_SS20_06_
assocname=SS20_MGWS2_06-MGWS2_SS20_06
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_07-MGWS2_SS20_07_
assocname=SS20_MGWS2_07-MGWS2_SS20_07
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_08-MGWS2_SS20_08_
assocname=SS20_MGWS2_08-MGWS2_SS20_08
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_09-MGWS2_SS20_09_
assocname=SS20_MGWS2_09-MGWS2_SS20_09
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_10-MGWS2_SS20_10_
assocname=SS20_MGWS2_10-MGWS2_SS20_10
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_11-MGWS2_SS20_11_
assocname=SS20_MGWS2_11-MGWS2_SS20_11
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_12-MGWS2_SS20_12_
assocname=SS20_MGWS2_12-MGWS2_SS20_12
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_13-MGWS2_SS20_13_
assocname=SS20_MGWS2_13-MGWS2_SS20_13
</logicallink>

<logicallink>
stacktype=IP
name=SS20_MGWS2_14-MGWS2_SS20_14_
assocname=SS20_MGWS2_14-MGWS2_SS20_14
</logicallink>


<logicallink>
stacktype=IP
name=SS20_MGWS2_15-MGWS2_SS20_15_
assocname=SS20_MGWS2_15-MGWS2_SS20_15
</logicallink>



</linkgroup>
</iuinterface>"""
