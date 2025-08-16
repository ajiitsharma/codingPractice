#!user/bin/env python3

from utils import TestRunner

# Constants
MOD = 10**9 + 7

def nCr_mod_fast(n: int, r: int) -> int:
    # C(n,r) = C(n-1,r-1) + C(n-1,r) --> This is O(n*r) time complexity
    # Better C(n,r) = C(n, r-1) * (n - r + 1) // r --> This is O(r) time complexity
    if r == 0:
        return 1
    if n < r or n <= 0 or r <= 0:
        return 0
        
    result = 1
    for i in range(1, r+1):
        result = result % MOD * (n-i+1) %MOD *(pow(i, MOD - 2, MOD)) % MOD
        
    return result % MOD
      

def solve(n, m):
    return nCr_mod_fast(m+n-2, m-1)



if __name__ == "__main__":
    runner = TestRunner(solve, description="Test runner for solve function.")
    runner.run_from_cli()

