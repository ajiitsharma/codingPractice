import math

'''
Given an integer n, compute the number of perfect squares that sum upto n.

INFO: Lagranges Four Square Theorem states that every natural number can be represented as the sum of four integer squares.
This means that for any integer n, there exist integers a, b, c, and d such that:
n = a^2 + b^2 + c^2 + d^2.
'''

class Solution:
    
    _MAX_SQUARES = math.inf # Placeholder for maximum squares, can be adjusted based on problem constraints

    def numSquares_recursive(self, n: int) -> int:
        """
        Calculate the minimum number of perfect square numbers which sum to n.
        
        :param n: The target integer
        :return: The minimum number of perfect square numbers that sum to n
        """
        if n <= 0:
            return 0
        
        max_range = int(n**0.5) + 1

        min_squares = self._MAX_SQUARES

        for i in range(max_range, 0, -1):
            curr = i * i
            target = n - curr

            if target == 0:
                return 1
            
            if target < 0:
                continue
            
            count_remaining = self.numSquares_recursive(target)

            if count_remaining != 0:
                min_squares = min(min_squares, count_remaining + 1)
        
        return min_squares
    
    def numSquares_dp(self, n: int) -> int:
        """        
        Calculate the minimum number of perfect square numbers which sum to n using dynamic programming.
        
        :param n: The target integer
        :return: The minimum number of perfect square numbers that sum to n
        """
        if n <= 0:
            return 0
        
        dp = [self._MAX_SQUARES] * (n + 1)
        dp[0] = 0  # Base case: 0 can be formed with 0 squares

        for i in range(1, n + 1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        
        return dp[n] if dp[n] != self._MAX_SQUARES else -1
        

def test_recursive():
    """
    Test function to validate the numSquares function.
    """
    solution = Solution()
    
    # Test cases
    test_cases = [0, 1, 2, 4, 5, 9, 13, 14, 110, 9292]
    
    for n in test_cases:
        result = solution.numSquares_recursive(n)
        print(f"The minimum number of perfect squares that sum to {n} is: {result}")

def test_dp():
    """
    Test function to validate the numSquares_dp function.
    """
    solution = Solution()
    
    # Test cases
    test_cases = [0, 1, 2, 4, 5, 9, 13, 14, 110, 9292]
    
    for n in test_cases:
        result = solution.numSquares_dp(n)
        print(f"The minimum number of perfect squares that sum to {n} is: {result}")

if __name__ == '__main__':
    test_dp()