'''
        https://leetcode.com/problems/sort-colors/description/

        You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

        You must solve this problem without using the library's sort function.

        Approach:
                3 pointer Dutch Flag Algorithm
'''

def get_sorted_colors(nums: list[int]) -> list[int]:

        # define 3 points
        low, mid, high = 0, 0, len(nums) - 1

        # run mid from low to high
        while mid <= high:
                if nums[mid] == 0:
                        nums[low], nums[mid] = nums[mid], nums[low]
                        low += 1
                        mid += 1
                elif nums[mid] == 1:
                        mid += 1
                elif nums[mid] == 2:
                        nums[mid], nums[high] = nums[high], nums[mid]
                        high -= 1

        return nums

if __name__ == '__main__':
        array = list(map(int, input("Enter the array: ").strip().split()))
        result = get_sorted_colors(array)

        print(f'The maximum size of the container = {result}')