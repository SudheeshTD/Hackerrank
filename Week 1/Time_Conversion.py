#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    sub = s.split(':')
    if(sub[2][2:] == "PM"):
        num = int(sub[0])
        if(num < 12):
            num = num + 12;
            new_time = str(num)
            sub[0] = new_time
            return sub[0]+":"+sub[1]+":"+sub[2][:2]
        else:
            return s[:-2]
            
    if(sub[2][2:] == "AM"):
        if(int(sub[0]) == 12):
            return "00:"+sub[1]+":"+sub[2][:2]
        else:
            return s[:-2]
        
            
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()



# def timeConversion(s):
#     hh=s[0:2]
#     if 'PM' in s:
#         hh=int(hh)+12 if hh!='12' else hh
#     else:
#         if hh=='12':
#             hh='00'
#     return (str(hh)+s[2:8])
     