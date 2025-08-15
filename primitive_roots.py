#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem: https://www.hackerrank.com/challenges/primitive-problem/problem?isFullScreen=true

Primitive root for a prime P is number g in [1,P-1] such that g^x mod P gives all [1,P-1], with x in [1,P-2]

Need to find:
    1. Smallest primitive root of p
    2. Total primitive roots of p

Solution logic: 
    1. determine all the prime factor of phi = p - 1 as p1, p2, ... pk
    2. For each candidate g
        for each prime factor pj
            if g^(phi/pj) mod != 1
        
        if above condition is met for all pj, it is a root

    3. Once one primitive root is found, others can be obtained as g^m where gcd(m, phi) == 1 i.e. they should be coprime
'''
def gcd_AB(a: int, b:int) -> int:
    if b > a:
        a, b = b, a
    if a%b == 0:
        return b
        
    return gcd_AB(b, a%b)

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

def get_prime_factors(n: int) -> set[int]:
    """Fast prime factorization using trial division up to sqrt(n)."""
    factors = set()

    while n % 2 == 0:
        factors.add(2)
        n //= 2

    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.add(f)
            n //= f
        f += 2

    if n > 1:
        factors.add(n)

    return factors

def primitive_root_check(g: int, phi_factors: list[int], p: int) -> bool:
    """Check if g is a primitive root modulo p."""
    return all(pow(g, (p - 1) // q, p) != 1 for q in phi_factors)

def primitive_roots(p: int) -> set[int]:
    """Find all primitive roots modulo p."""
    phi_factors = list(get_prime_factors(p - 1))

    # Find smallest primitive root
    for g in range(2, p):
        if primitive_root_check(g, phi_factors, p):
            primitive = g
            break

    # Generate all primitive roots from the smallest one
    roots = {pow(primitive, k, p) for k in range(1, p) if gcd_AB(k, p - 1) == 1}
    return roots
    
if __name__ == '__main__':
    p = int(input().strip())
    primitive_roots_list = primitive_roots(p)
    print(primitive_roots_list)
    print (min(primitive_roots_list), len(primitive_roots_list))
    
