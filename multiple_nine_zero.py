#!user/bin/env python3

import math
import os
import random
import re
import sys

def compute_mutiple(n: int) -> int:
    """
    This function computes the least number formed of 9s and 0s that is the multiple of n
    
    :param n: An integer to check for multiples
    :return: The least number formed of 9s and 0s that is a multiple of n
    """
    if n == 0:
        return 0
    
    curr = 1
    
    while True:
        curr_decimal = 9*int(bin(curr)[2:])  # Convert binary to decimal
        if curr_decimal % n == 0:
            return curr_decimal
        else:
            curr += 1
    
    return 9*int(bin(curr)[2:])


def main() -> None:
    """
    Main function to test the compute_mutiple function with sample input.
    """
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 777777]
    
    for n in test_cases:
        result = compute_mutiple(n)
        print(f"Least number formed of 9s and 0s that is a multiple of {n}: {result}")  

if __name__ == "__main__":
    main()