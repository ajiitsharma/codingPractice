'''
        https://codeforces.com/problemset/problem/1097/D

        Given an N integer N following steps are performed K times.
                1. Get all the divisors of N, 1 and N inclusive
                2. Replace N with any divisor D from the divisors of N
                3. All divisors have equal probability of being selected.

        Find the expected value or the number on the backboard after K steps

        Approach:
                1. Divisor set be D[j] := D[0] = 1 and D[M - 1] = N with total of M divisors 
                2. DC[j] = number of divisors of each divisor j
                3. Define DP[i, j] as the probability of getting divisor D[j] after step k
                4. D[i, j] = sum(D[i-1, j] * (1/DC[w]) for all w such that D[j]*w <= N
                5. Answer = sum of probabilitiesof the last row
'''

import math
MOD = 10**9 + 7

def mod_inverse(n: int) -> int:
        return pow(n, MOD - 2, MOD)

def get_prime_factorization(N: int) -> list[tuple[int, int]]:
        primes = []
        target = N
        for j in range(2, math.isqrt(N) + 1):
                if target == 1:
                       break
                if target % j == 0:
                        k = 0
                        while target % j == 0:
                                k += 1
                                target //= j
                        primes.append((j, k))

        if target != 1:
               primes.append((target, 1))

        return primes


def get_expectation_single_prime(P: int, m: int, K: int) -> int:
        '''
        Computes expected value E[P^X] after K steps starting from P^m using standard floats.
        '''

        # Precompute modular inverses for 1 / (e + 1)
        inv = [mod_inverse(i) for i in range(m + 2)]


        # DP[e] stores probability of having exponent e at current step
        # Step 0: exponent is m with probability 1.0
        dp = [0] * (m + 1)
        dp[m] = 1

        for step in range(1, K + 1):
                next_dp = [0] * (m + 1)
                for e in range(m + 1):
                # To end at exponent e, previous exponent e_prev must be >= e
                # Transition probability from e_prev to e is 1 / (e_prev + 1)
                        for e_prev in range(e, m + 1):
                                prob = (dp[e_prev] * inv[e_prev + 1]) % MOD
                                next_dp[e] = (next_dp[e] + prob) % MOD
                dp = next_dp

        # Expectation = sum(P^e * P(X = e))
        expectation = 0
        for e in range(m + 1):
                p_pow_e = pow(P, e, MOD)
                contribution = (p_pow_e * dp[e]) % MOD
                expectation = (expectation + contribution) % MOD
                
        return expectation

def solve_makoto(N: int, K: int) -> int:
        factors = get_prime_factorization(N)
        total_expectation = 1
        
        for p, m in factors:
                exp_p = get_expectation_single_prime(p, m, K)
                total_expectation = (total_expectation * exp_p) % MOD
                
        return total_expectation

if __name__ == '__main__':
        N, K = list(map(int, input().strip().split()))
        result = solve_makoto(N, K)
        print(result)