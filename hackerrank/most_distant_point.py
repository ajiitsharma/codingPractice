#! user/bin/env/python3

import math

'''
Problem: https://www.hackerrank.com/challenges/most-distant/problem?isFullScreen=true
'''

class Point():
        def __init__(self, x: int, y:int) -> None:
                self.x = x
                self.y = y

        def dist(self, other):
                return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
        def __repr__(self):
                return f'({self.x}, {self.y})'

def max_distance_in_grid(grid: list[Point]) -> int:
        max_xp, max_xn, max_yp, max_yn = 0, 0, 0, 0
        for point in grid:
                if point.x == 0 and point.y > 0:
                        max_yp = max(max_yp, point.y)
                if point.x == 0 and point.y < 0:
                        max_yn = max(max_yn, -point.y)
                if point.y == 0 and point.x > 0:
                        max_xp = max(max_xp, point.x)
                if point.y == 0 and point.x < 0:
                        max_xn = max(max_xn, -point.x)

        farthest_points = [Point(max_xp, 0), Point(-max_xn, 0), Point(0, max_yp), Point(0, -max_yn)]
        max_dist = 0

        for i in range(4):
                for j in range(i, 4):
                        max_dist = max(max_dist, farthest_points[i].dist(farthest_points[j]))

        return max_dist

if __name__ == '__main__':
        n = int(input().strip())
        grid = []
        for _ in range(n):
                x,y = map(int, input().strip().split())
                new_point = Point(x, y)
                grid.append(new_point)
        
        max_distance = max_distance_in_grid(grid)
        print(max_distance)