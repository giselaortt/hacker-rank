#URL of the problem:
#https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-six
#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import *

def cookies(k, A):
    heapify(A)
    numberOfOperations = 0

    while( len(A) >= 2 and A[0] < k  ):
        smallest = heappop( A )
        secondSmallest=heappop( A )
        newValue = smallest + 2*secondSmallest
        heappush(A, newValue)
        numberOfOperations = numberOfOperations+1

    if( len(A) == 0 ):
        numberOfOperations = -1

    if( len(A) == 1 and A[0] < k ):
        numberOfOperations = -1

    return numberOfOperations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
