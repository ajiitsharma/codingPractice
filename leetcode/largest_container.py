'''
        https://leetcode.com/problems/container-with-most-water/description/
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.
'''

import math

def get_max_container_area(array: list[int]) -> int:

        # two pointer solution
        left = 0
        right = len(array) - 1
        max_area = 0

        while left < right:
                max_area = max(max_area, (right - left)*min(array[left], array[right]))

                if array[left] < array[right]:
                        left += 1
                else:
                        right -= 1
                
        
        return max_area

if __name__ == '__main__':
        array = list(map(int, input("Enter the array: ").strip().split()))
        result = get_max_container_area(array)

        print(f'The maximum size of the container = {result}')