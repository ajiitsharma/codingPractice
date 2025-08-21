import math

'''
Problem: https://www.hackerrank.com/challenges/eulers-criterion/problem?isFullScreen=true
If a = x^2 mod m where x in Zm, a will have quadratic residue iff a^((m-1)/2) == 1 mod m
'''

def fast_exponent(x: int, n: int, mod: int) -> int:

        if x == 0:
               return 0

        m = abs(n)
        base, result = x, 1

        while m:
            if m % 2 != 0:
                result = (result * base) % mod

            base = (base * base) % mod
            m //=2
        
        return result % mod

def check_quadratic_residue(a: int, m: int) -> str:
        if fast_exponent(a, (m-1)//2, m) == 1 or a == 0:
                return 'YES'
        return 'NO'

if __name__ == '__main__':
        print(check_quadratic_residue(0,41))