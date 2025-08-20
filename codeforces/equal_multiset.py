import math
from collections import Counter

'''
Problem: https://codeforces.com/problemset/problem/2131/C
Need to optimize it.
'''

def isMultisetEqual(S: list[int], T: list[int], k: int) -> bool:

        n = len(S)
        if n != len(T):
                return False
        
        # residue counts
        cntS = Counter([x % k for x in S])
        cntT = Counter([x % k for x in T])
        
        # check residue 0
        if cntS[0] != cntT[0]:
                return False
        
        # if k is even, check k/2 residue
        if k % 2 == 0:
                if cntS[k//2] != cntT[k//2]:
                        return False
        
        # check residue pairs (i, k-i)
        for i in range(1, (k+1)//2):
                if i == k - i:  # skip the middle when k even (already checked)
                        continue
                if cntS[i] + cntS[k-i] != cntT[i] + cntT[k-i]:
                        return False
        
        return True

if __name__ == '__main__':
        t = int(input().strip())
        for _ in range(t):
                n, k = map(int, input().strip().split())
                S = list(map(int, input().strip().split()))
                T = list(map(int, input().strip().split()))

                if isMultisetEqual(S, T, k):
                        print('YES')
                else:
                        print('NO')
