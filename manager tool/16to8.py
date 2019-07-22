#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import datetime
import os
import shutil

import cv2

##############################
d1 = datetime.datetime.now()
##############################



filepath="F:/tf/zmap/p3/u16/"
filepathto=filepath[:-1]+"u8/"

if(os.path.exists(filepathto)==False):
    os.mkdir(filepathto) 


pathDir =  os.listdir(filepath)
for allDir in pathDir:
    imagepath=filepath+allDir
    imagepathto=filepathto+allDir
##    print(imagepath)

    #16uc1 open
    sMat = cv2.imread(imagepath,2)

    #change 8uc1
    sMat = cv2.normalize(src=sMat, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    #save png
    cv2.imwrite(imagepathto, sMat, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])


    
    print(allDir)



##imagepath="F:/tf/zmap/p3/u16/2019-3-20 13-56-46.dt.PNG"
##imagepathto="F:/tf/zmap/p3/u16/a.dt.PNG"



###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
