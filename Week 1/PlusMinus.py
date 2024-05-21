#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pve = 0;
    nve = 0;
    zer = 0;
    for i in arr:
        if i<0:
            nve += 1
        elif i == 0:
            zer += 1
        else:
            pve +=1
        
    print("{:.6f}".format(pve / len(arr)))
    print("{:.6f}".format(nve / len(arr)))
    print("{:.6f}".format(zer / len(arr)))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
