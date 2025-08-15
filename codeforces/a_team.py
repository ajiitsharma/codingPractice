#!user/bin/env python3

'''
Codeforce problem set: https://codeforces.com/problemset/problem/231/A
'''


if __name__ == '__main__':
        n = int(input().strip())
        count = 0
        for j in range(n):
                a, b, c = map(int, input().strip().split())
                if a+b+c >= 2:
                        count += 1
                
        print(count)
