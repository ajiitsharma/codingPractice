#!/bin/python3

import math
import os
import random
import re
import sys

def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 ==0 or n% 3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6

    return True

def primitive_roots(p:int) -> list[int]:
    candidates = []

    residues = set(range(1, p))
    for g in range(2, p):
        resids = set()
        for x in range(p-1):
            resids.add(g**x % p)

        if resids.issubset(residues) and resids.issuperset(residues):
             candidates.append(g)

    return candidates
    
if __name__ == '__main__':
    p = int(input().strip())
    primitive_roots_list = primitive_roots(p)
    print(primitive_roots_list)
    print (min(primitive_roots_list), len(primitive_roots_list))
