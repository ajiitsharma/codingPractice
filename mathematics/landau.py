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

def gcd_AB(a: int, b:int) -> int:
        if b > a:
                a, b = b, a

        if b == 0:
                return a
        
        if a%b == 0:
                return b
                
        return gcd_AB(b, a%b)


def lcm_AB(a: int, b:int) -> int:
       return a*b//gcd_AB(a, b)


def is_prime(n: int) -> bool:
        if n == 0:
                return False
        
        if n <= 3:
                return True
        
        if n % 2 == 0 or n % 3 == 0:
                return False
        
        j = 5
        while j*j <= n:
                if n % j == 0 or n % (j + 2) == 0:
                        return False
                
                j += 6

        return True


def compute_landau(N: int) -> list[int]:
        # to complete this method

        prime_powers = [(j, math.floor(math.log(N)/ math.log(j))) for j in range(2, math.ceil(math.sqrt(N)) + 1) if is_prime(j)]

        landau = [1]*(N+1)

        return landau


def create_partitions_brute(N: int) -> list[list[int]]:
        print(f'Computing partition for N = {N}')

        if N == 1:
                return [[1]]
        
        partitions = []
        for j in range(N-1, 0, -1):
                prev_partition = create_partitions_brute(j)
                for row in prev_partition:
                        row.append(N-j)
                        partitions.append(row)

        partitions.append([N])
        return partitions
        
def create_partitions_brute_memo(N: int, memo: dict[int, list[int]] = None) -> list[list[int]]:

        if memo is None:
                memo = {}

        if N == 1:
                memo[1] = [[1]]
                return memo[1]
        
        if N in memo:
                return memo[N]
        
        partitions = []
        for j in range(N-1, 0, -1):
                prev_partition = create_partitions_brute_memo(j, memo)
                for row in prev_partition:
                        partitions.append(row + [N-j])

        partitions.append([N])
        memo[N] = partitions
        
        return memo[N]


def compute_landau_dp_1D(N: int) -> list[int]:
        dp = [0] * (N+1)
        dp[0] = 1
        for n in range(1, N+1):
                best = 1
                for k in range(1, n+1):
                        best = max(best, lcm_AB(k, dp[n-k]))
                dp[n] = best
        return dp



if __name__ == '__main__':
        # print(f'Program to compute Landau function g(N)')
        # max_range = int(input('Enter N: ').strip())

        # landau = compute_landau_dp_1D(max_range)
        # for i, val in enumerate(landau):
        #         print(f'g({i}) = {val}')

        print(f'Program to create partition of N')
        max_range = int(input('Enter N: ').strip())
        partitions  = create_partitions_brute_memo(max_range)
        for row in partitions:
                print(row)


        