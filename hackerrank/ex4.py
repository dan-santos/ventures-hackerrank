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
    positive = 0
    negative = 0
    zeros = 0
    
    for element in arr:
        if element > 0:
            positive += 1
        elif element < 0:
            negative += 1
        else:
            zeros += 1
    
    positive /= len(arr)
    negative /= len(arr)
    zeros /= len(arr)

    return f'{positive:.6f}\n{negative:.6f}\n{zeros:.6f}'

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))
