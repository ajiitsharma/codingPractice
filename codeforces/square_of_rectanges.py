#! user/bin/env python3

'''
Problem: https://codeforces.com/problemset/problem/2120/A
'''

def isSquarePossible(l1: int, l2: int, l3: int, b1: int, b2: int, b3: int) -> bool:
        if l1 == l2 == l3:
                if b1 + b2 + b3 == l1:
                        return True

        if b1 == b2 == b3:
                if l1 + l2 + l3 == b1:
                        return True

        if l1 == l2 + l3:
                if b2 == b3 and b2 + b1 == l1:
                        return True

        if b1 == b2 + b3:
                if l2 == l3 and l2 + l1 == b1:
                        return True

        return False

if __name__ == '__main__':
        t = int(input().strip())
        for _ in range(t):
                l1, b1, l2, b2, l3, b3 = map(int, input().strip().split())
                solution = isSquarePossible(l1, l2, l3, b1, b2, b3)
                print(f'{'YES' if solution else 'NO'}')