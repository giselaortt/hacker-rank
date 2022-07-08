
## https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one


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
    numberOfPositives = 0
    numberOfNegatives = 0
    numberOfZeros = 0

    for element in arr:
        if element > 0 :
            numberOfPositives = numberOfPositives + 1

        if element < 0 :
            numberOfNegatives = numberOfNegatives + 1

        if element == 0:
            numberOfZeros = numberOfZeros + 1

    ratioPositive = numberOfPositives / len(arr)
    ratioNegative = numberOfNegatives / len(arr)
    ratioZeros = numberOfZeros / len(arr)
    print("%.6f" % ratioPositive + '\n', '%.6f' % ratioNegative + '\n', '%.6f'%ratioZeros + '\n' )

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

