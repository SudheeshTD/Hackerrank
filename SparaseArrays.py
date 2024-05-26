#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#



def matchingStrings(strings, queries):
    # Write your code here
    dictn = {}
    queryDict = []
    stringsLen = len(strings)
    for i in strings:
        if(i in dictn):
            dictn[i] +=1
        else:
            dictn[i] = 1
    
    for i in queries:
        if i in dictn:
            queryDict.append(dictn[i])
        else:
            queryDict.append(0)
            
    return queryDict
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
