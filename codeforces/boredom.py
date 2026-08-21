'''
        https://codeforces.com/problemset/problem/455/A

        Given a sequence a consisting of n integers. The player can make several steps. In a single step he can choose an element of the sequence (let's denote it ak) and delete it, at that all elements equal to ak + 1 and ak -1 also must be deleted from the sequence. That step brings ak points to the player.

        Alex is a perfectionist, so he decided to get as many points as possible. Help him.
'''
from collections import Counter

def get_best_score(nums: list[int], N: int) -> int:
        min_num, max_num = min(nums), max(nums)

        # precompute frequency
        freq = Counter(nums)

        dp = [0] * (max_num + 1)

        for j in range(1, max_num + 1):
                dp[j] = max(dp[j-1], dp[j-2] + j*freq[j])

        return dp[max_num]

if __name__ == '__main__':
        n = int(input())
        array = list(map(int, input().strip().split()))

        max_score = get_best_score(array, n)
        print(max_score)