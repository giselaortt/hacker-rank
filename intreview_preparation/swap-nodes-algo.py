#https://www.hackerrank.com/challenges/swap-nodes-algo/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
import sys
sys.setrecursionlimit(15000)


def traversal( tree, currentNode, answer ):
    leftChild =  tree[ currentNode ][0]
    if( leftChild != -1 ):
        traversal( tree, leftChild, answer )
    answer.append( currentNode )
    rightChild = tree[ currentNode ][1]
    if( rightChild != -1 ):
        traversal( tree, rightChild, answer )


def swapChildren( tree, nodeIndex ):
    tree[ nodeIndex ] = ( tree[ nodeIndex ][1], tree[ nodeIndex ][0] )


def calculateHeights( tree ):
    #could create a dictionary that contains a list with every node on that height
    heights = [-1]*len( tree )
    heights[1] = 1
    myqueue = deque()
    myqueue.append( 1 )
    while( len( myqueue ) > 0 ):
        currentNode = myqueue.popleft()
        leftChild = tree[ currentNode ][ 0 ]
        rightChild = tree[ currentNode ][ 1 ]

        if( leftChild != -1 ):
            heights[ leftChild ] = heights[ currentNode ] + 1
            myqueue.append(leftChild)

        if( rightChild != -1 ):
            heights[ rightChild ] = heights[ currentNode ] + 1
            myqueue.append( rightChild )

    return heights


def getHeights( heights, k ):
    answer = []
    for height, i in zip(heights, range(len(heights))):
        if( height % k == 0 ):
            answer.append( i )

    return answer


def swapNodes( tree, queries):
    heights = calculateHeights( tree )
    answer = []
    for query in queries:
        toBeSwaped = ( getHeights( heights, query ) )
        for swapIndex in toBeSwaped :
            swapChildren( tree, swapIndex )
        tra = []
        traversal( tree, 1, tra )
        answer.append( tra )
    
    return answer


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    indexes.insert( 0, (0,0) )
    queries_count = int(input().strip())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print( '\n'.join([' '.join(map(str, x)) for x in result]) )
    #fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()
