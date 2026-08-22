'''
        https://codeforces.com/problemset/problem/313/B

        Count all matches between two given index 
        Match is a[i] == a[i+1]
'''

def get_match_count(string: str) -> list[int]:
        N = len(string)
        matches = [0] * N

        for j in range(N - 1):
                if string[j] == string[j+1]:
                        matches[j] = 1

        prefix_sum = [0] * N

        for j in range(1, N):
                prefix_sum[j] = prefix_sum[j -1] + matches[j - 1]
        return prefix_sum

if __name__ == '__main__':
        string = str(input())
        cases = int(input())

        prefix = get_match_count(string)
        for _ in range(cases):
                l, r = list(map(int, input().strip().split()))
                print(prefix[r-1] - prefix[l-1])
        