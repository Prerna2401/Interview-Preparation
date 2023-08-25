from os import *
from sys import *
from collections import *
from math import *

def pairSum(ARR, S):
    result = []
    frequency = {}
    
    for num in ARR:
        complement = S - num
        
        if complement in frequency:
            count = frequency[complement]
            result.extend([[num, complement]] * count)
        
        frequency[num] = frequency.get(num, 0) + 1
    
    for pair in result:
        pair.sort()
        
    result.sort()  # Sort the pairs
    
    return result