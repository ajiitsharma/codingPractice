#!/bin/python3

import math
import os
import random
import re
import sys



def primitive_roots(n:int) -> list[int]:
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
