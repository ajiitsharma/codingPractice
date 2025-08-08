#!/usr/bin/env python3

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        diff_dict = {}

        for j, n in enumerate(nums):
            diff_dict[n] = j

        j = 0
        while True:
            if target - nums[j] in diff_dict:
                target_index = diff_dict[target - nums[j]]

                if j == target_index:
                    j+=1
                else:
                    return [j, target_index]
            else:
                j += 1

        return []
    
if __name__ == '__main__':
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
    # Expected output: [0, 1] since nums[0] + nums[1] = 2 + 7 = 9