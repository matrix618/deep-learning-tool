import re
import os
import time


while 1:
    f = os.popen('C:/Program Files/NVIDIA Corporation/NVSMI/nvidia-smi.exe', 'r')
    s1 = f.read()

    h1=s1.find('+')
    strtime=s1[:h1]
    print(strtime)
    
    h2=s1.find('N/A')
    s1=s1[h2+6:]
    h3=s1.find('+')
    strinfo=s1[:h3]
    print(strinfo)

    with open("D:/temp/nvi5.txt","a") as texta:
        texta.write(strtime)
        texta.write(strinfo)
    
    time.sleep(10)

