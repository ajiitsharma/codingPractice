#! user/bin/env python3

'''
Problem: https://codeforces.com/contest/2120/problem/B
'''

def count_collission(ball_count: int, pool_size: int, grid: list[list[int]]) -> int:
        count = 0

        # for each ball check if its tragectory lies on the diagonals
        for row in grid:
                vel_x, vel_y = row[0], row[1]
                loc_x, loc_y = row[2], row[3]

                # if it lies on y = x axis dot product of radius and velocity vector must not be zero
                if loc_x == loc_y:
                        if loc_x*vel_x + loc_y*vel_y != 0:
                                count += 1
                
                # if it lies on the y = -x axis
                if loc_y == pool_size - loc_x:
                        if (loc_x - pool_size)*vel_x + (loc_y)*vel_y != 0:
                                count += 1
        return count

if __name__ == '__main__':
        t = int(input().strip())
        for _ in range(t):
                ball_count, pool_size = map(int, input().strip().split())
                grid = []
                for j in range(ball_count):
                        dx, dy, x, y = map(int, input().strip().split())
                        grid.append([dx, dy, x, y])
                solution = count_collission(ball_count, pool_size, grid)
                print(solution)