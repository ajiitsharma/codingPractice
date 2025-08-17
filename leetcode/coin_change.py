#! user/bin/env python3

import math
from collections import deque
'''
Problem: https://leetcode.com/problems/coin-change/description/

Create a 2D array coins[M][N] where coins[i][j] denotes the min number of coins required to reach value i using coin set [0,1,... j-1, j]
Initialize the coins matrix with inf
DP step:
        coins[i][j]     = min(i//j + coins[i % coin_value[j] ][j], coins[i][j-1]) if i >= coin_val[j] !!! This does not work as we're greedy forcing it to take max number of jth coins
                        = coins[i][j] = min(coins[i][j-1], 1 + coins[i - coin_value[j]][j])
                        = coins[i][j-1] if i < j
Boundary Conditions:
        for i = 0 coins[0][j] = 0 for all j

return coins[M-1][N-1] if != inf else -1
'''

def min_coin_change_2D(amount: int, coin_value: list[int]) -> int:
        coin_value = sorted(coin_value)

        M, N = amount+1, len(coin_value)
        coins = [[math.inf for _ in coin_value] for _ in range(M)]

        for j in range(N):
                coins[0][j] = 0

        for i in range(M):
                for j in range(N):
                        if i >= coin_value[j]:
                                coins[i][j] = min(coins[i][j-1], 1 + coins[i - coin_value[j]][j]) #knapsack type, with jth coin and without jth coin
                        else:
                                coins[i][j] = coins[i][j-1]

        return coins[M-1][N-1] if coins[M-1][N-1] != math.inf else -1


def min_coin_change_1D(amount: int, coins: list[int]) -> int:
    ''' 1D space optimization'''
    dp = [math.inf] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != math.inf else -1


def min_coin_change_bfs(amount: int, coins: list[int]) -> int:
        ''' BFS Implementation '''
        if amount == 0:
                return 0

        queue = deque([(0, 0)])  # (current_sum, steps)
        visited = set([0])       # track visited sums

        while queue:
                current_sum, steps = queue.popleft()

                for coin in coins:
                        nxt = current_sum + coin

                        if nxt == amount:
                                return steps + 1  # found solution
                        
                        if nxt < amount and nxt not in visited:
                                visited.add(nxt)
                                queue.append((nxt, steps + 1))

        return -1  # no solution

def test() -> None:
        test_cases = [
                {'coins': [1,2,5], 'target': 11},
                {'coins': [2,5], 'target': 3},
                {'coins': [2], 'target': 0},
                {'coins': [186,419,83,408], 'target': 6249}
        ]

        for case in test_cases:
                print(min_coin_change_2D(case['target'], case['coins']))

if __name__ == '__main__':
        test()