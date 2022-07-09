#URL:
#https://www.hackerrank.com/challenges/one-week-preparation-kit-no-prefix-set/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-seven

#!/bin/python3

import math
import os
import random
import re
import sys


'''
def generateAllPrefixes( word ):
    answer = set()
    for i in range( len(word) ):
        answer.add( word[ : i ] )

    return answer
'''
##  The big question here is, how to generate only the minimal amount of prefixes that i will need ?
## TML with this solution with 2 hashtables on 7 testcases.

if __name__ == '__main__':
    n = int(input().strip())
    words = set()
    prefixes = set()
    answer = "GOOD SET"

    for _ in range(n):
        newWord = input().strip()

        if( newWord in words or newWord in prefixes ):
            answer = "BAD SET\n"+newWord
            break
        
        else:
            words.add( newWord )
            '''
            newPrefixes = generateAllPrefixes( newWord )

            if( newPrefixes & words ):
                answer = "BAD SET\n"+newWord
                break

            prefixes = prefixes.union( newPrefixes ) 

    print(answer)


