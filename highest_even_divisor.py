#!/usr/bin/env python3

import math

'''
    Given a number n, find the total number of even divisors of n
'''

def even_divisor_count_slow(n):
    # find all even divisors of n, so checking upto n//2
    # time complexity is O(n/2) = O(n)
    count = 0
    for j in range(2, n//2 +1, 2):
        if n % j == 0 and j % 2 == 0    :
            count += 1

    return count

def even_divisor_count_fast(n):
    
    # get all divisors upto sqrt(n)
    # time complexity is O(sqrt(n))
    divs = {i for i in range(2,int(math.sqrt(n))+1) if n%i==0} 
    
    # add the corresponding divisors n//i and n itself
    divs = divs | {n//i for i in divs} | {n} 

    # filter out odd divisors
    return sum(1 for d in divs if d % 2 == 0)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = even_divisor_count_fast(num)
    if result:
        print(f"Number of even divisors of {num} is {result}.")
    else:
        print(f"{num} has no even divisors.")