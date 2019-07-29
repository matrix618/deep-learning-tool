 
import re
import os

import time

#5 second run cmd NVSMI
while 1:
    f = os.popen('C:/Program Files/NVIDIA Corporation/NVSMI/nvidia-smi.exe', 'r')
    s = f.read()
    print(s)
    time.sleep(5)
