#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import shutil


import imgtopology

def xml_name(s1):
    h1=s1.find("<name>")

    li=[]

    while h1>0:

        s1=s1[h1+6:]
        h1=s1.find("<")
        
        sname=s1[:h1] 
        
        h1=s1.find("<xmin>")
        s1=s1[h1+6:]
        h1=s1.find("</xmin>")
        xmin=int(s1[:h1])
        h1=s1.find("<ymin>")
        s1=s1[h1+6:]
        h1=s1.find("</ymin>")
        ymin=int(s1[:h1])
        h1=s1.find("<xmax>")
        s1=s1[h1+6:]
        h1=s1.find("</xmax>")
        xmax=int(s1[:h1])
        h1=s1.find("<ymax>")
        s1=s1[h1+6:]
        h1=s1.find("</ymax>")
        ymax=int(s1[:h1])
    
        li.append([sname,xmin,ymin,xmax,ymax])

        h1=s1.find("<name>")

    return li



##############################
d1 = datetime.datetime.now()
##############################

filepath="D:/ftp/CVIS_SW_IREC/picture/2019-07-19-BGV5000/bgp_png_V5000/"
filepath1="D:/ftp/CVIS_SW_IREC/picture/2019-07-19-BGV5000/bgp_png_V5000_1/"

#stype="bottle"
stype="smoke"

i=0

isum=0
isum_=0

false_alarm1=0
missed1=0

false_alarm2=0
missed2=0

#miss_

pathDir =  os.listdir(filepath)
for allDir in pathDir:
    if(allDir[:4]!="high"):continue
    if(allDir[-3:]!="xml"):continue

    icon1=0
    icon2=0

    icon1_1=0
    icon2_1=0

#    with open(filepath+allDir) as opentext:
#        for line in opentext.readlines():
#            if(line.find("<name>bottle")>-1):icon1=icon1+1
#            if(line.find("<name>smoke")>-1):icon2=icon2+1
#
#    with open(filepath1+allDir) as opentext:
#        for line in opentext.readlines():
#            if(line.find("<name>bottle")>-1):icon1_1=icon1_1+1
#            if(line.find("<name>smoke")>-1):icon2_1=icon2_1+1
    
    list1,list2=[],[]

    with open(filepath+allDir) as opentext:
        s1=opentext.read()
        list1=xml_name(s1)

    with open(filepath1+allDir) as opentext:
        s1=opentext.read()
        list2=xml_name(s1)

    #print(list1)
    #print(list2)

    for element1 in list1:

        if element1[0] != stype:continue
        isum=isum+1
        
        #print([element1[1],element1[2],element1[3],element1[4]])
        iele=0
        for element2 in list2:

            if element2[0] != stype:continue

            im=imgtopology.rectangle_lap(element1[1],element1[2],element1[3],element1[4],element2[1],element2[2],element2[3],element2[4])

            if im>iele:
                iele=im
        #print("ele:"+str(iele))

        if iele<0.2:
            missed1=missed1+1
            print(allDir)


    for element2 in list2:

        if element2[0] != stype:continue
        isum_=isum_+1

        iele=0
        for element1 in list1:

            if element1[0] != stype:continue

            im=imgtopology.rectangle_lap(element2[1],element2[2],element2[3],element2[4],element1[1],element1[2],element1[3],element1[4])

            if im>iele:
                iele=im
        #print("ele_false:"+str(iele))

        if iele<0.2:
            false_alarm1=false_alarm1+1
            print(allDir)

    #break

print(missed1)
print(false_alarm1)

print(isum)
#print(isum_)

print("missed rate:"+ str(missed1/isum))
print("false rate:"+ str(false_alarm1/isum)+"(right rate:"+ str(1-false_alarm1/isum)+")")


#i=imgtopology.rectangle_lap(100,300,200,400,100,50,200,350)

#print(false_alarm1)
#print(false_alarm2)

###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
