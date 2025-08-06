#!/bin/python3

import math
import os
import random
import re
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_square_tile(l, b):    
    areaMax = l*b
    singleTileArea = gcd(l, b) ** 2

    return areaMax//singleTileArea
            
if __name__ == '__main__':
    test_cases = [
        (4, 6),
        (10, 10),
        (5, 3),
        (8, 2),
        (12, 15)
    ]
    
    for l, b in test_cases:
        result = max_square_tile(l, b)
        print(f"Result for dimensions ({l}, {b}): {result}")
        # Expected outputs: 6, 10, 3, 2, 15