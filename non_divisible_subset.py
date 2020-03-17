#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# https://www.hackerrank.com/challenges/non-divisible-subset/problem
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    permut = defaultdict(list)
    result = [0]*k # for elements
    res = [[] for _ in range(k)] # for remains
    for e in s:
        permut[e%k].append(e)
    for v,e in permut.items():
        for i in range(k):
            if i + v != k:
                if v not in res[i]:
                    if (v == 0 or v==k/2.0) and len(e)>0:
                        result[i] += 1
                        res[i].append(k-v)
                    else:
                        result[i] += len(e)
                        res[i].append(k-v)
                else:
                    if len(e) > len(permut.get(k-v,[])):
                        result[i] += len(e) - len(permut.get(k-v,[]))
                        res[i].append(k-v)
                        res[i].remove(v)
    return max(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
