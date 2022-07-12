#URL:
#https://www.hackerrank.com/challenges/one-week-preparation-kit-no-prefix-set/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-seven

#!/bin/python3

import math
import os
import random
import re
import sys


def no_prefix():
    n = int(input().strip())
    words = set()
    prefixes = set()
    answer = "GOOD SET"

    for _ in range(n):
        newWord = input().strip()
        #print("\n"+newWord)
        if( newWord in words or newWord in prefixes ):
            answer = "BAD SET\n"+newWord
            return answer

        words.add( newWord )
        newPrefix = ''
        for char in newWord[:-1] :
            newPrefix = newPrefix + char
            #print(newPrefix)
            if( newPrefix in words  ):
                answer = "BAD SET\n"+newWord
                return answer
            prefixes.add( newPrefix )

    return answer


if __name__ == '__main__':
    print( no_prefix() )


