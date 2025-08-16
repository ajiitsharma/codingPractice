#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def gcd_AB(a: int, b:int) -> int:
    if b > a:
        a, b = b, a
    if a%b == 0:
        return b
        
    return gcd_AB(b, a%b)
        
def gcd_list(nums:list[int]) -> int:
    if len(nums) == 1:
        return nums[-1]
        
    list_gcd_val = gcd_AB(nums[0], nums[1])
    j = 2
    
    while j < len(nums):
        if list_gcd_val == 1:
            return list_gcd_val
            
        list_gcd_val = gcd_AB(list_gcd_val, nums[j])
        j += 1
        
    return list_gcd_val
    
    
def solve(a:list[int]) -> str:
    if len(a) <= 1:
        return 'NO'
    
    for j in range(1, len(a)):
        if gcd_list(a[:j]) == 1:
            return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
