'''
Odd Selection

Shubham has an array  of size n, and wants to select exactly x elements from it, such that their sum is odd. These elements do not have to be consecutive. The elements of the array are not guaranteed to be distinct.

Tell him whether he can do so.

'''

def if_odd_sum(array: list[int], N: int, X: int) -> bool:
        odds, evens = 0, 0
        for j, num in enumerate(array):
                if num%2 == 0:
                        evens += 1
                else:
                        odds += 1

        curr_odd = X - 1 if X % 2 == 0 else X

        while curr_odd >= 1:
                curr_even = X - curr_odd
                if evens - curr_even >= 0 and odds - curr_odd >= 0:
                        return True
                else:
                        curr_odd -= 2
        return False

if __name__ == '__main__':
        cases = int(input())
        for _ in range(cases):
                n, x = map(int, input().strip().split())
                array = list(map(int, input().strip().split()))

                result = if_odd_sum(array, n, x)
                print(f'Yes' if result else 'No')