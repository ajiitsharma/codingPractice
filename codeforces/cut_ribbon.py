'''
        https://codeforces.com/problemset/problem/189/A

        Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:

        After the cutting each ribbon piece should have length a, b or c.
        After the cutting the number of ribbon pieces should be maximum.
        Help Polycarpus and find the number of ribbon pieces after the required cutting.

'''

def get_max_pieces(N: int, a: int, b: int, c: int) -> int:
        dp = [0] * (N+1)

        for j in range(1, N + 1):
                for k in [a, b, c]:
                        if j - k == 0:
                                dp[j] = max(dp[j], 1 + dp[j - k])
                        elif j - k > 0 and dp[j - k ] != 0:
                                dp[j] = max(dp[j], 1 + dp[j - k])


                        # print(f'{j}-{k}-{dp}')
        return dp[N]

if __name__ == '__main__':
        n, a, b, c = map(int, input().strip().split())
        result = get_max_pieces(n, a, b, c)

        print(result)