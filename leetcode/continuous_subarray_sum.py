#!user/bin/env python3
import math
import itertools
from collections import defaultdict

'''
https://leetcode.com/problems/continuous-subarray-sum/description/

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and the sum of the elements of the subarray is a multiple of k.

Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

'''


class Solution:
        def checkSubarraySum(self, nums: list[int], target: int) -> bool:
                remainderMap = {0:-1}
                prefixSum = itertools.accumulate(nums)

                for j, num in enumerate(nums):
                        pass

                return 0



        

if __name__=='__main__':
        print(f'Enter the array')
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        count = Solution().checkSubarraySum(arr, target)
        print(f'Total number of subarrays = {count}')
