'''
        Problem: https://codeforces.com/problemset/problem/2247/A

        Given an array of length n consisting of only +1 or -1
        Operation allowed: for any index i you can change ai -> -ai and ai+1 -> -ai+1 together
        Operation can be performed any number of times.

        determine whether it is possible to get a sum of all elements equal to 0.

        Approach:
                Let S be the sum of the array.
                for any operation perfomed the sum changes by 4
                So for S = 0 => S mod 4 === 0
                Further if the length is odd, S can never become 0
'''

def if_zero_sum(array: list[int], n: int) -> str:
        if n % 2 == 0 and sum(array) % 4 == 0:
                return 'YES'
        return 'NO'

if __name__ == '__main__':
        cases = int(input())

        for _ in range(cases):
                n = int(input())
                array = list(map(int, input().strip().split()))
                result = if_zero_sum(array, n)
                print(result)