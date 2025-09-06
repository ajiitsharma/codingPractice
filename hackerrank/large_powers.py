#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**9 + 7

def power(base, exp, modulus):
    # Implements modular exponentiation
    res = 1
    base %= modulus
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % modulus
        base = (base * base) % modulus
        exp //= 2
    return res

def large_mod(num_str, modulus):
    # Calculates num_str % modulus for large num_str
    res = 0
    for digit_char in num_str:
        res = (res * 10 + int(digit_char)) % modulus
    return res

def solve(A_str, B_str):

    a_val = large_mod(A_str, MOD)
    b_effective = large_mod(B_str, MOD - 1)

    if b_effective == 0 and a_val != 0:
        result = 1
    elif b_effective == 0 and a_val == 0:
        result = 0 # 0^very_large_positive_number is 0
    else:
        result = power(a_val, b_effective, MOD)
        
    return result

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        a = first_multiple_input[0]

        b = first_multiple_input[1]

        result = solve(a, b)

        print(result)

