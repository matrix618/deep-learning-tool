#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import shutil


##############################
d1 = datetime.datetime.now()
##############################

filepath="D:/ftp/CVIS_SW_IREC/picture/2019-07-19-BGV5000/bgp_png_V5000/"
filepath1="D:/ftp/CVIS_SW_IREC/picture/2019-07-19-BGV5000/bgp_png_V5000_1/"

i=0

false_alarm1=0
missed1=0

false_alarm2=0
missed2=0

pathDir =  os.listdir(filepath)
for allDir in pathDir:
    if(allDir[:4]!="high"):continue
    if(allDir[-3:]!="xml"):continue

    icon1=0
    icon2=0

    icon1_1=0
    icon2_1=0

    with open(filepath+allDir) as opentext:
        for line in opentext.readlines():
            if(line.find("<name>bottle")>-1):icon1=icon1+1
            if(line.find("<name>smoke")>-1):icon2=icon2+1

    with open(filepath1+allDir) as opentext:
        for line in opentext.readlines():
            if(line.find("<name>bottle")>-1):icon1_1=icon1_1+1
            if(line.find("<name>smoke")>-1):icon2_1=icon2_1+1

    #print(allDir+":"+str(icon1))
    print(allDir+":"+str(icon1)+"->"+str(icon1_1)+":"+str(icon2)+"->"+str(icon2_1))
    
    if(icon1_1>icon1):
        false_alarm1=false_alarm1+icon1_1-icon1
        
    if(icon2_1>icon2):
        false_alarm2=false_alarm2+icon2_1-icon2



###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
