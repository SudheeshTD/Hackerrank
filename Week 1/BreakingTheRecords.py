#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#




def breakingRecords(scores):
    # Write your code here
    best = scores[0]
    worst = scores[0]
    maxRec, minRec = 0,0
    
    for nums in scores:
        if(nums > best):
            best = nums
            maxRec += 1
        if(nums < worst):
            worst = nums
            minRec += 1
        else:
            continue
    return maxRec, minRec
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
