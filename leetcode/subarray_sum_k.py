#!user/bin/env python3
import math
import itertools
from collections import defaultdict

'''
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

'''

class Solution:
        def countSubarray(self, arr: list[int], target: int) -> int:
                if len(arr) == 0:
                        return 0
                
                cumSumCounts = defaultdict(int)
                cumSumCounts[0] = 1    # this is key here

                currentSum = 0
                counter = 0

                for j in range(len(arr)):
                        currentSum += arr[j]

                        targetDiff = currentSum - target
                        if targetDiff in cumSumCounts:
                                counter += cumSumCounts[targetDiff]
                        
                        cumSumCounts[currentSum] += 1

                return counter
        

if __name__=='__main__':
        print(f'Enter the array')
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        count = Solution().countSubarray(arr, target)
        print(f'Total number of subarrays = {count}')
