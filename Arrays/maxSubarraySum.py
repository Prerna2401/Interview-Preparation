from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit,maxsize
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    start, end = 0, 0
    s = 0
    max_so_far = -maxsize-1
    max_ending_here = 0
    for i in range(n):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
        if max_so_far < 0:
            max_so_far = 0
    return max_so_far

#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
