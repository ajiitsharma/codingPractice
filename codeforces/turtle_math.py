'''
        https://codeforces.com/problemset/problem/1933/B

        Objective is to make the sum of sum elements divisible by 3 in minimum number of moves

        1 move = either 
                increase value of 1 element by 1
                remove an element from the array

        Return minimum moves + 0 moves is possible
'''

import math

def compute_min_moves(nums: list[int], N: int) -> int:
        # for empty array
        if not nums:
                return 0

        S = sum(nums)

        if S % 3 == 0:
                return 0

        if S % 3 == 2:
                return 1

        # if S % 3 == 1, then we will have to either add 2 or remove an element aj such that aj % 3 == 1
        for num in nums:
                if num % 3 == 1:
                        return 1
        return 2

if __name__ == '__main__':
        T = int(input())
        for _ in range(T):
                N = int(input())
                nums = list(map(int, input().strip().split()))

                result = compute_min_moves(nums, N)
                print(result)