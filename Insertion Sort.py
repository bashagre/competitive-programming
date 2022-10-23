#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    temp = arr[-1]
    for i in range(len(arr)-1,-1,-1):
        if i == 0:
            arr[i] = temp
            print(*arr, sep=' ')
            break

        elif arr[i]>=temp and arr[i-1]>temp:
            #print(arr[i],">=",temp)
            arr[i] = arr[i-1]
            print(*arr, sep=' ')  
        
        
        elif arr[i]>=temp and arr[i-1]<temp:
            #print("found")
            #print(i)
            arr[i] = temp
            print(*arr, sep=' ')
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
