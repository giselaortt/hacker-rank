# https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

#!/bin/python3

import math
import os
import random
import re
import sys


#the logic behind this code is simple, it comes from the assumption that the minimal number of swapes that orders the array equals the number os swapes that mixed it.


def minimumBribes(q):
    for element, i in zip(q, range(len(q))) :
        if( element - i -1 > 2 ):
            print("Too chaotic")
            return
    
    totalNumberOfBrides = 0
    ordered = False
    while( not ordered ):
        ordered = True
        #print(q)
        for i in range( len(q)-1 ):
            if(q[i+1] < q[i] ):
                q[i], q[i+1] = q[i+1], q[i]
                totalNumberOfBrides = totalNumberOfBrides+1
                ordered = False
            
    print(totalNumberOfBrides)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

