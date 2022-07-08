#URL:
#https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-four


#!/bin/python3

import math
import os
import random
import re
import sys



def gridChallenge(grid):

    print(grid)

    for i in range(len(grid)) :
        grid[i] = list(grid[i])
        grid[i].sort()

    print(grid)

    numberOfRows = len(grid)
    numberOfColums = len(grid[0])

    for i in range( numberOfColums ):
        for j in range( numberOfRows -1 ):
            if( grid[j][i] > grid[j+1][i] ):
                return "NO"

    return "YES"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

