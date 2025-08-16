#!/bin/python3

import math
import os
import random
import re
import sys


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
        
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True

    
def primeCount(n):
    if n == 0:
        return 0
        
    if n in [2,3]:
        return 1

    count = 0
    primeReach = 1
    i = 2
    while primeReach*i <= n:
        if isPrime(i):
            primeReach *= i
            count += 1
        i+=1
    return count



if __name__ == '__main__':
    test_cases = [0,1,2,3,5,10,20,50,100,500,10000,10000,100000000]

    for n in test_cases:
        result = primeCount(n)
        # print(f"Result for {n} (primeCount): {result}")
        print(f"Result for {n} (primeFactorsCount): {result}")
        