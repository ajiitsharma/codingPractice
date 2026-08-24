'''
        https://codeforces.com/problemset/problem/1832/B

        You have to make K moves
        in each move either
                1. remove two smallest elements
                2. Remove the largest element

        return the maximum sum after K moves
'''

import math

def get_maximum_sum(nums: int, N: int, K: int) -> int:

        # first sort the array
        nums_sorted = sorted(nums)

        cumsum = [0] * N
        curr_sum = 0
        for j, n in enumerate(nums_sorted):
                curr_sum += n 
                cumsum[j] = curr_sum

        l, r = -1, N - 1 - K
        max_sum = 0
        while r <= N - 1:
                if l == -1:
                        interval_sum = cumsum[r]
                else:
                        interval_sum = cumsum[r] - cumsum[l]
                max_sum = max(max_sum, interval_sum)

                r += 1
                l += 2


        return max_sum

if __name__ == '__main__':
        T = int(input())
        for _ in range(T):
                N, K = list(map(int, input().strip().split()))
                nums = list(map(int, input().strip().split()))

                result = get_maximum_sum(nums, N, K)
                print(result)