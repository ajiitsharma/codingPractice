#!/usr/bin/env python3

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left_index, right_index = 0, (len(numbers) -1)

        while left_index < right_index:
            diff = target - (numbers[left_index] + numbers[right_index])

            if diff == 0:
                return [left_index, right_index]

            elif diff > 0:
                left_index += 1
            
            else:
                right_index -= 1
        
        return [left_index, right_index]  # Fallback, should not happen for valid inputminor 
    
if __name__ == '__main__':
    # Example usage
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(numbers, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
    # Expected output: [0, 1] since numbers[0] + numbers[1] = 2 + 7 = 9
        