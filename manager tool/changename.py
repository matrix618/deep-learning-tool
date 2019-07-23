#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import datetime

import cv2

import os

##############################
d1 = datetime.datetime.now()
##############################

file_dir=r'N:\ftp\CVIS_SW_IREC\test\jiu2_3011\png0.3'

##for root, dirs, files in os.walk(file_dir):  


for root, dirs, files in os.walk(file_dir):  
##    print(files)
    t=1
    for f1 in files:
        #print(f1[:-4]+'.0.6'+f1[-4:])
        newname1=f1[:-4]+'.0.3'+f1[-4:]
        t=t+1
        os.rename(root+'\\'+f1,root+'\\'+newname1)


###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
