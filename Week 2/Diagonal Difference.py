#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    ri,rj,li,lj = 0,len(arr)-1,0,0
    rcount,lcount = 0,0
    
    for i in range(len(arr)):
        
        rcount += arr[ri][rj]
        lcount += arr[li][lj]
        ri,rj = ri+1,rj-1
        li,lj = li+1,lj+1

    return abs(rcount-lcount)
        


#print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
