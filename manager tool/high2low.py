#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import shutil


##############################
d1 = datetime.datetime.now()
##############################

filepath="D:/ftp/CVIS_SW_IREC/picture/2019-05-06-BGV5000/bgp_png_V5000/"

i=0

##pathDir =  os.listdir(filepathto)
##for allDir in pathDir:
##    child = os.path.join('%s%s' % (filepathto, allDir))
##    os.remove(child)

pathDir =  os.listdir(filepath)
for allDir in pathDir:
    
    if(allDir[-3:]=="xml"):

        if(allDir[:4]!="high"):continue

        print(allDir)
        
        allDir1="low"+allDir[4:]

##        shutil.copyfile(filepath+allDir,filepath+allDir1)

        with open(filepath+allDir1,"w") as texta0:texta0.write("")

        with open(filepath+allDir) as opentext:
            for line in opentext.readlines():  
                with open(filepath+allDir1,"a") as texta:
                    line=line.replace("high","low")
                    texta.write(line)  


        
print(i)






###############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
