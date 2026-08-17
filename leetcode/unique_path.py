import math

def number_of_paths(grid:list[list[int]]) -> int:
        if not grid or not grid[0]:
                return 0

        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
                return 0

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        # initialize the first row
        for j in range(1, n):
                dp[0][j] = 1 if grid[0][j] == 0 and dp[0][j - 1] == 1 else 0

        # initialize the first column
        for j in range(1, m):
                dp[j][0] = 1 if grid[j][0] == 0 and dp[j - 1][0] == 1 else 0

        # fill the remaining dp cells
        for i in range(1, m):
                for j in range(1, n):
                        if grid[i][j] == 1:
                                dp[i][j] = 0

                        else:
                                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m -1][n - 1]

if __name__ == '__main__':
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        result = number_of_paths(obstacleGrid)

        print(f'The total number of paths = {result}')