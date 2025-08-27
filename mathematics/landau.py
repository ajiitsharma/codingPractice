#!user/bin/env/python3

import math

'''
Program to compute Landau function g(N) := The maximum order of an element of a finite symmetric group -> maximum LCM of the partition of n
Partition of N - ways of writing N as sum of k , 1<= k <= N
Eg: 5   = 5                     LCM = 5
        = 4 + 1                 LCM = 4
        = 3 + 2                 LCM = 6 <- Maximal LCM
        = 3 + 1 + 1             LCM = 3
        = 2 + 2 + 1             LCM = 2
        = 2 + 1 + 1 + 1         LCM = 2
        = 1 + 1 + 1 + 1 + 1     LCM = 1

g(n) can be computed using DP paradigm.
g(0) = 1 , base case
g(j) = max(j, g())
'''
def gcd_AB(a: int, b: int) -> int:
        if a <= b:
                a, b = b, a
        
        if b == 0:
                return a

        if b == 1:
                return 1
        
        return gcd_AB(b, a%b)

def lcm_AB(a: int, b: int) -> int:
        
        return a*b//gcd_AB(a, b)

def compute_landau(N: int) -> list[int]:
        landau = [1]*(N+1)

        for i in range(1, N + 1):
                maximal_i = 1
                for j in range(1, i//2 + 1):
                        maximal_i = max(maximal_i, lcm_AB(landau[j], landau[i - j]))
                maximal_i = max(maximal_i, i)
                landau[i] = maximal_i
        return landau

if __name__ == '__main__':
        print(f'Program to compute Landau function g(N)')
        max_range = int(input('Enter N: ').strip())

        landau = compute_landau(max_range)
        for i, val in enumerate(landau):
                print(f'g({i}) = {val}')