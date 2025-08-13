import math

'''
Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)) where m and n are the sizes of the two arrays.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)

        expected_median_index = (m +n + 1) // 2
        sorted_array = []

        i, j = 0, 0
        while i + j < expected_median_index:
            if i < m and (j >= n or nums1[i] < nums2[j]):
                sorted_array.append(nums1[i])
                i += 1
            else:
                sorted_array.append(nums2[j])
                j += 1

        print(f"Sorted array up to median index: {sorted_array}")
        print(f"Final indices: i={i}, j={j}")
        return 0.0
    

if __name__ == '__main__':
    # Example usage
    nums1 = [1, 3]
    nums2 = [2]
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"The median of the two sorted arrays is: {result}")
    # Expected output: 2.0 since the combined sorted array is [1, 2, 3] and the median is 2.0
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f"The median of the two sorted arrays is: {result}")
    # Expected output: 2.5 since the combined sorted array is [1, 2, 3, 4] and the median is (2 + 3) / 2 = 2.5