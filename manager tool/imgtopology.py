#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import os
import shutil


##############################
d1 = datetime.datetime.now()
##############################

#two rectangle lap rate
#first rectangle xmin,ymin,xman,ymax
#second rectangle xmin_,ymin_,xman_,ymax_
def rectangle_lap(xmin,ymin,xmax,ymax,xmin_,ymin_,xmax_,ymax_):
    txmin,txmax,tymin,tymax=0,0,0,0

    if xmin<xmin_:
        txmin=xmin_
    else:
        txmin=xmin

    if xmax<xmax_:
        txmax=xmax
    else:
        txmax=xmax_

    if ymin<ymin_:
        tymin=ymin_
    else:
        tymin=ymin

    if ymax<ymax_:
        tymax=ymax
    else:
        tymax=ymax_

    if txmax<txmin:
        return 0

    if tymax<tymin:
        return 0

    area=(xmax-xmin)*(ymax-ymin)
    tarea=(txmax-txmin)*(tymax-tymin)

    area_rate=tarea/area

    return area_rate


i=rectangle_lap(100,300,200,400,100,50,200,350)
print(i)


##############################    
d2 = datetime.datetime.now()
print(d2-d1)
##############################
