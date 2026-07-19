#!user/bin/env/python3
import math

class Solution:
        def findMonotonicTriplet(self, arr: list[int]) -> list[int]:
                N = len(arr)
                leftMin = [-1]*N
                rightMax = [-1]*N

                currMin = 0
                for j in range(1, N):
                        if arr[j] <= arr[currMin]:
                                currMin = j
                        else:
                                leftMin[j] = currMin

                currMax = N-1
                for j in range(N-2, -1, -1):
                        if arr[j] >= arr[currMax]:
                                currMax = j
                        else:
                                rightMax[j] = currMax

                for j in range(N):
                        if leftMin[j] != -1 and rightMax[j] != -1:
                                return [leftMin[j], j, rightMax[j]]

                return []

if __name__ == '__main__':
        print('Enter the array elements separated by spaces:')
        arr = list(map(int, input().strip().split()))
        
        result = Solution().findMonotonicTriplet(arr)
        
        if result:
                i, j, k = result
                print(f'Monotonic Triplet Indices are {i}, {j}, {k}')
                print(f'Values are {arr[i]}, {arr[j]}, {arr[k]}')
        else:
                print('No monotonic triplet found.')
