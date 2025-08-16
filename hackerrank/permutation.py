#! /usr/bin/env python3

import math

'''
        Given a string S of N 0's and M 1's, how many unique permutations of this string start with 1?

'''

MOD = 10**9 + 7

def count_combinations(n: int, r: int) -> int:
      # C(n,r) = C(n-1,r-1) + C(n-1,r) --> This is O(n*r) time complexity
      # Better C(n,r) = C(n, r-1) * (n - r + 1) // r --> This is O(r) time complexity
      if r == 0:
          return 1
      if n < r or n <= 0 or r <= 0:
          return 0
      
      # Using a list to store the combination values
      combination_array = [1] * (r+1)
      combination_array[1] = n
      
      for i in range(2, r+1):
          combination_array[i] = (combination_array[i-1] * (n - i + 1) // i)% MOD
      
      return combination_array[r]       

if __name__ == "__main__":
    # Example usage
    test_cases = [
        (1,1),  # 1 0 and 1 1
        (2,3),  # 2 0's and 3 1's
        (5, 3),  # 5 0's and 3 1's
        (10, 5), # 10 0's and 5 1's
        (7, 2),  # 7 0's and 2 1's
        (6, 4)   # 6 0's and 4 1's
    ]
    
    for n, m in test_cases:
        result = count_combinations(n + m - 1, n)
        print(f"Number of unique permutations starting with 1 for {n} 0's and {m} 1's: {result}")
    
