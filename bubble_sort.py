# solution to https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n = len(a)
    numSwaps = 0
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if(a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1
            j += 1
        i += 1
        
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
