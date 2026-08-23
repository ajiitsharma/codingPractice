'''
        https://codeforces.com/contest/2257/problem/D

        Given S = area of rectangle
        Consider all possible set of rectangles with one vetrex at 0, 0 having area S => R(S)
        for a query (x, y) forming a rectange of area xy with opposite vertices at (0,0) and (x,y)
        find the number of cells in the intersection of area between query rectange and R(S)

        Approach:
                first find all (a, b) such that ab = S
                sort by a to get a list [(a, b)]
                for each number j from 1 to x:
                        find the height h[j] using binary search on [(a, b)] taking value from right if exact match not found
                        i.e. if a[i] < j < a[i+1] => h[j] = b[j + 1]
                return sum(h[j])
'''

import math

def get_rectangle_sides(S: int) -> list[tuple[int, int]]:
        # find the list of set (a, b) such that a * B = S
        valid_sides = []
        sq_x = math.ceil(math.sqrt(S))
        for j in range(1, sq_x + 1):
                if S % j == 0:
                        valid_sides.append((j, S//j))

                        if j * j != S:
                                valid_sides.append((S//j, j))

        # sort the list by x coodinate
        valid_sides = sorted(valid_sides, key = lambda x: x[0])        

        return valid_sides

def binary_search_index(side_pairs: list[tuple[int]], target: int) -> int:
        # need binary search for index just greater than j
        left, right = 0, len(side_pairs) - 1
        first_valid_index = -1

        while left <= right:
                mid = (left + right) // 2
                if side_pairs[mid][0] >= target:
                        first_valid_index = mid
                        right = mid - 1
                else:
                        left = mid + 1

        return first_valid_index

def find_common_area_step_method(S: int, cases: list[list[int]]) -> list[int]:

        valid_sides = get_rectangle_sides(S)
        max_x = valid_sides[-1][0]

        intersect_area = []

        for test_rect in cases:
                test_X, test_Y = test_rect
                total_area = 0
                curr_X = 1

                for a_i, b_i in valid_sides:
                        if curr_X > test_X:
                                break

                        right_X = min(a_i, test_X)

                        if curr_X <= right_X:
                                width = right_X - curr_X + 1
                                height = min(b_i, test_Y)
                                total_area += width * height
                                curr_X = right_X + 1


                intersect_area.append(total_area)

        return intersect_area

def find_common_area_binary_search(S: int, cases: list[list[int]]) -> list[int]:

        valid_sides = get_rectangle_sides(S)
        max_x = valid_sides[-1][0]

        intersect_area = []

        for test_rect in cases:
                test_rect_X, test_rect_Y = test_rect
                total_area = 0
                # fill the height array
                height_for_x = [0] * (test_rect_X + 1)

                limit_x = min(test_rect_X, max_x)

                for j in range(limit_x + 1):
                        if j == 0:
                                continue

                        # linear search for index just greater than j
                        # valid_x_index = [i for i, x in enumerate(valid_sides) if x[0] >= j]

                        # binary search
                        index_j = binary_search_index(valid_sides, j)

                        if index_j == -1:
                                height = 0
                        else:
                                height = valid_sides[index_j][1]

                        total_area += min(test_rect_Y, height)

                intersect_area.append(total_area)

        return intersect_area

if __name__ == '__main__':
        N = int(input())

        for _ in range(N):
                S, T = list(map(int, input().strip().split()))
                cases = []
                for j in range(T):
                        x, y = list(map(int, input().strip().split()))
                        cases.append([x,y])
                result = find_common_area_step_method(S, cases)

                for res in result:
                        print(res)