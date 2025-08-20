MOD = 10**9 + 7  # prime modulus

def precompute_factorials(n, MOD):
    fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = (fact[i-1] * i) % MOD
    
    invfact = [1] * (n+1)
    invfact[n] = pow(fact[n], MOD-2, MOD)  # Fermat’s little theorem
    for i in range(n, 0, -1):
        invfact[i-1] = (invfact[i] * i) % MOD
    
    return fact, invfact

def nCr_mod(n, r, fact, invfact, MOD):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n-r] % MOD


if __name__ == "__main__":
    N = 10**6  # up to 1e6
    fact, invfact = precompute_factorials(N, MOD)
    
    # Example queries
    print(nCr_mod(10, 3, fact, invfact, MOD))   # 120
    print(nCr_mod(1000000, 500000, fact, invfact, MOD))  # huge but O(1)