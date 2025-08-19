#!user/bin/env/python3

'''
Problem: https://www.hackerrank.com/challenges/littlepandapower/submissions/code/444243313
Find a^b mod x - Here gcd(a, x) == 1
If b > 0 we can use Russian Peasant method (fast exponentiation)
If b < 0, we would require multiplicative inverse of a
        a^(-m) mod x = (a^m)^-1 mod x or (a^-1)^m mod x

To find multiplicative inverse we need to find solution to az = 1 mod x. Because gcd(a, x) == 1
        1 = s * a + t * x => as = (1 - tx) mod x => as = 1 mod x
Method to find s and t -> Extended Euclid Algorithm : same process of Euclid Algorithm to find gcd
'''

def extended_gcd(a, x):
        # Keep track of coefficients
        old_r, r = a, x
        old_s, s = 1, 0
        old_t, t = 0, 1
        
        while r != 0:
                quotient = old_r // r
                old_r, r = r, old_r - quotient * r
                old_s, s = s, old_s - quotient * s
                old_t, t = t, old_t - quotient * t
        
        # old_r is gcd, old_s and old_t are the coefficients
        return old_r, old_s, old_t  # gcd, s, t

def fast_exponent(x: int, n: int, mod:int) -> int:
        m = abs(n)
        base, result = x, 1

        while m:
            if m % 2 != 0:
                result = (result * base) % mod

            base = (base ** 2) % mod
            m //=2
        
        return result

def solve(a: int, b: int, x: int) -> int:
      gcd, s, t = extended_gcd(a, x)
      print(extended_gcd(a, x), s%x)
      result = fast_exponent(a, b, x) if b > 0 else fast_exponent(s%x, abs(b), x)

      return result

if __name__ == '__main__':
      print(solve(4, -1, 5))

