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

filepath="F:/tf/zmap/p10/temp1/"


i=0

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


aw=np.asarray(iw)
ah=np.asarray(ih)

print(aw)
print(ah)


print("meanw:"+str(np.mean(aw)))
print("meanh:"+str(np.mean(ah)))

print("stdw:"+str(np.std(aw)))
print("stdw:"+str(np.std(ah)))

###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
