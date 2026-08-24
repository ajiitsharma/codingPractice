'''
        https://codeforces.com/problemset/problem/1206/B

        You are given n numbers a1, a2, ... an
        With a cost of one coin you can perform the following operation:

                Choose one of these numbers and add or subtract 1 from it.
                In particular, we can apply this operation to the same number several times.
        We want to make the product of all these numbers equal to 1
                i.e. a1*a2*...an = 1

        What is the minimum cost to do so?
'''

def compute_min_cost(nums: list[int], n: int) -> int:

        if not nums:
                return -1
        # a 2D array, one row for each num in nums
        # row j [0] -> cost to get aj to -1
        # row j [1] -> cost to get aj to +1
        # row j [2] -> total cost to prod -1
        # row j [3] -> total cost to prod +1
        dp = [[0, 0, 0, 0] for _ in range(n)]

        # base case for 0th 
        dp[0][0] = abs(-1 - nums[0])
        dp[0][1] = abs( 1 - nums[0])
        dp[0][2] = abs(-1 - nums[0])
        dp[0][3] = abs( 1 - nums[0])

        for j in range(1, n):
                dp[j][0] = abs(-1 - nums[j])
                dp[j][1] = abs( 1 - nums[j])

                # net cost to get to -1
                # equals min(cost to get aj to -1 and total cost till j-1 to +1, cost to get aj to +1 and total cost till j-1 to -1)
                dp[j][2] = min(dp[j][0] + dp[j - 1][3], dp[j][1] + dp[j-1][2])

                # net cost to get to +1
                # equals min of (cost to get aj to -1 and total cost till j-1 to -1, cost to get aj to +1 and total cost till j-1 to +1)
                dp[j][3] = min(dp[j][0] + dp[j - 1][2], dp[j][1] + dp[j - 1][3])

                # print(dp[:j+1])
        return dp[n-1][3]

if __name__ == '__main__':
        n = int(input())
        nums = list(map(int, input().strip().split()))

        min_cost = compute_min_cost(nums, n)
        print(min_cost)