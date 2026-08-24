'''
        https://codeforces.com/problemset/problem/9/A

'''

import math

def solve(r1: int, r2: int) -> str:
        winning_rolls = 7 - max(r1, r2)
        total = 6

        common = math.gcd(winning_rolls, total)

        return f'{winning_rolls // common}/{total // common}'

if __name__ == '__main__':
        r1, r2 = list(map(int, input().strip().split()))
        result = solve(r1, r2)
        print(result)