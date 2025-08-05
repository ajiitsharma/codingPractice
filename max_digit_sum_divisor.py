#!/bin/python3

import math
import os
import random
import re
import sys

stoiMap = {}

def computeStringSum(n):
    string = str(n)
    print(f"String representation of {n}: {string}")
    intVal = 0
    for s in string:
        intVal += stoiMap[s]
        
    return intVal
    
def computeBestDivisor(n):
    divisor_list = [1]
    maxDigitSum = 0
    for i in range(2, n+1):
        if n%i == 0:
            currDigitSum = computeStringSum(i)
            
            if currDigitSum > maxDigitSum:
                divisor_list = [i]
                maxDigitSum = currDigitSum
            elif currDigitSum == maxDigitSum:
                divisor_list.append(i)
            else:
                continue
    
    return min(divisor_list)
            

if __name__ == '__main__':
    n = int(input().strip())
    for i in range(10):
        stoiMap[str(i)] = i
    print(computeBestDivisor(n))

