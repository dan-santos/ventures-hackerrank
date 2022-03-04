# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here

    # checando se as listas tem o mesmo tamanho.
    if(len(a) != len(b)):
        return None
    else:
        # Cria com notas zeradas para os participantes.
        notas = [0, 0]
        # criamos um zip com as duas listas        
        for(nota_a, nota_b) in zip(a, b):
            if nota_a > nota_b:
                notas[0] += 1
            elif nota_a < nota_b:
                notas[1] += 1
        return notas
     

                
            




if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()