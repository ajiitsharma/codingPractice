#!user/bin/env python3
import math

'''
Problem: https://leetcode.com/problems/minimum-path-sum/description/

Create a 2D matrix cost[x][y] where
        cost[i][j] denote the total sum cost till that point in grid (its own value inclusive)
For any i,j
        cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
Boundary conditions
        cost[0][0] = grid[0][0]
        if i == 0 cost[i][j] = cost[i][j-1] + grid[i][j]
        if j == 0 cost[i][j] = cost[i-1][j] + grid[i][j]
'''

MAX = math.inf

def min_path_sum(grid: list[list[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        cost = [[MAX for _ in range(N)] for _ in range(M)]

        #boundary case
        cost[0][0] = grid[0][0]

        for i in range(1, M):
                cost[i][0] = cost[i-1][0] + grid[i][0]

        for j in range(1, N):
                cost[0][j] = cost[0][j-1] + grid[0][j]

        for i in range(1, M):
                for j in range(1, N):
                        cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
        
        return cost[M-1][N-1]

def test() -> None:
        test_cases = [
                [[1,3,1],[1,5,1],[4,2,1]],
                [[1,2,3],[4,5,6]]
        ]

        for case in test_cases:
                solution = min_path_sum(case)
                print(f'{solution}')

if __name__ == '__main__':
        test()