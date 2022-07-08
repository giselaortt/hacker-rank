#https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-five
#!/bin/python3

import math
import os
import random
import re
import sys
#import queue
from collections import deque

def isOpenBracket( char ):
    
    if( char == '{' or char == '[' or char == '(' ):
        return True
    
    return False


def doesBracketsMatch( first, second ):
    
    if( first == '[' and second == ']' ):
        return True
    if( first == '{' and second == '}' ):
        return True
    if( first == '(' and second == ')' ):
        return True
    
    return False


def isBalanced(s):
    #mystack = queue.LifoQueue()
    mystack = deque()
    mystack.clear()
    answer = "YES"
    
    for bracket in s:
        if( isOpenBracket(bracket) ):
            #mystack.put(bracket)
            mystack.append(bracket)
        else:
            #nextBracket = mystack.get()
            if( len(mystack) == 0 ):
                answer = "NO"
                break
            nextBracket = mystack.pop()
            if( not doesBracketsMatch( nextBracket, bracket ) ):
                answer =  "NO"
                break
    
    if( len(mystack) > 0 ): 
        answer = "NO"
    
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
