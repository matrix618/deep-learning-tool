#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import shutil

import numpy as np
from PIL import Image


##############################
d1 = datetime.datetime.now()
##############################

filepath="F:/tf/zmap/p10/temp2/"


i=0

##pathDir =  os.listdir(filepathto)
##for allDir in pathDir:
##    child = os.path.join('%s%s' % (filepathto, allDir))
##    os.remove(child)

iw=[]
ih=[]

pathDir =  os.listdir(filepath)
for allDir in pathDir:
    
    if(allDir[-3:]=="xml"):continue

    print(filepath+allDir)

    image=Image.open(filepath+allDir)
    (im_width, im_height) = image.size

    print(im_width, im_height)

    iw.append(im_width)
    ih.append(im_height)


print(iw)
print(ih)



    
##    with open(filepath+allDir1,"w") as texta0:texta0.write("")
##
##    with open(filepath+allDir) as opentext:
##        for line in opentext.readlines():  
##            with open(filepath+allDir1,"a") as texta:
##                line=line.replace("high","low")
##                texta.write(line)  

   
print(i)


###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
