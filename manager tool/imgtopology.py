#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import shutil


##############################
d1 = datetime.datetime.now()
##############################

#first rectangle xmin,ymin,xman,ymax
#second rectangle xmin_,ymin_,xman_,ymax_
def rectangle_lap(xmin,ymin,xman,ymax,xmin_,ymin_,xman_,ymax_):
    txmin,tmax
    if(xmin<xmin_):
        txmin=xmin_
    else:
        txmin=xmin

    return txmin





i=rectangle_lap(1,1,1,3,2,2,2,4)
print(i)


##############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
