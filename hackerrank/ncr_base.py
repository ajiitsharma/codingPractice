import math

MOD = 1000_000_000
def binomial_mod_fast(n: int) -> list[int]:
        # C(n,r) = C(n-1,r-1) + C(n-1,r) --> This is O(n*r) time complexity
        # Better C(n,r) = C(n, r-1) * (n - r + 1) // r --> This is O(r) time complexity

        result = [1]*(n+1)
        for i in range(1, n//2 + 1):
                result[i] = (result[i-1] * (n - i + 1)//i)
                result[n-i] = result[i]
                
        return [j%MOD for j in result]

if __name__ == '__main__':
        t = int(input().strip())
        for _ in range(t):
                n = int(input().strip())
                print(f'{' '.join(map(str, binomial_mod_fast(n)))}')

