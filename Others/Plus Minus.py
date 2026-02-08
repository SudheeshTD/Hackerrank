#!/bin/python3
# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

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
    poss = 0
    neg = 0
    zeros = 0
    tot_nums = len(arr)
    
    for i in arr:
        if i == 0:
            zeros+= 1
        elif i < 0:
            neg += 1
        else:
            poss += 1
    
    print(f"{poss/tot_nums:.6f}")
    print(f"{neg/tot_nums:.6f}")
    print(f"{zeros/tot_nums:.6f}")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
