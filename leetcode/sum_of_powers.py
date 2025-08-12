class Solution:
    
    _MOD = 10**9 + 7
    
    def maxRange(self, n: int, x: int) -> int:
        """
        This function calculates the maximum base `i` such that `i^x <= n`.
        It returns the largest integer `i` for which this condition holds.
        """
        if n < 0 or x <= 0:
            return 0
        
        i = 1
        while i**x <= n:
            i += 1
        
        return i - 1
    

    def numberOfWays(self, n: int, x: int) -> int:

        if n < 0 or x <= 0:
            return 0
        
        if n == 0:
            return 0
        
        if n == 1:
            return 1 if x >= 1 else 0
        
        if x == 1:
            return 1 if n >= 0 else 0
        
        count = 0
        
        maxRange = Solution.maxRange(self, n, x)

        # Iterate from the maximum base down to 1
        # This ensures we count larger bases first, which helps in avoiding duplicates
        # and ensures we find all unique combinations.
        
        for i in range(maxRange, 1, -1):
            curr = i**x
            target = n - curr

            if target == 0:
                count += 1
                continue
            
            if target < 0:
                continue
            
            # Recursive call to find the number of ways for the remaining target
            count_remaining = Solution.numberOfWays(self, target, x)

            if count_remaining != 0:
                count += count_remaining
        
        return count%self._MOD
    
    def numberofWaysDP(self, n: int, x: int) -> int:
        """
        This function calculates the number of ways to express `n` as a sum of powers of integers raised to `x`.
        It uses dynamic programming to build up the solution.
        """

        maxRange = Solution.maxRange(self, n, x)
        if maxRange == 0:
            return 0
        if n < 0 or x <= 0:
            return 0
        
        # Create a DP array to store the number of ways to express each number
        # dp[i][j] will store the number of ways to express `i` using bases up to `j`
        
        dp = [[0] * (maxRange+1) for _ in range(n + 1)]
        # Base case:
        for j in range(maxRange + 1):
            dp[0][j] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, maxRange+1):
                base_power = j ** x
                if base_power > i:
                    dp[i][j] = dp[i][j - 1]  # Cannot use this base, carry forward the previous count
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - base_power][j - 1]  # Include or exclude the current base
        
        print(f"DP Table for n={n}, x={x}:")
        for i, row in enumerate(dp):
            print(f"{i}: {row}")

        return dp[n][maxRange]%self._MOD

def main():
    """
    Main function to test the numberOfWays function with sample input.
    """
    # Example usage
    n = [4, 10, 27]
    x = 3  # Power to which the base is raised
    print(f"Calculating number of ways to express {n} as a sum of powers of {x}:")
    
    # Create an instance of the Solution class
    if isinstance(n, list):
        for num in n:
            solution = Solution()
            result = solution.numberOfWays(num, x)
            print(f"Number of ways to express {num} as a sum of powers of {x}: {result}")
    else:
        pass

def test():
        """
        Test function to validate the numberOfWays and numberofWaysDP functions.
        """
        # Testing the DP function
        dp_test_cases = [
                (4, 1, 2),
                (4, 3, 0),
                (5, 2, 1),
                (10, 3, 0),
                (10, 2, 1),
        ]
        
        solution = Solution()
        for n, x, expected in dp_test_cases:
            result_dp = solution.numberofWaysDP(n, x)
            assert result_dp == expected, f"DP Test failed for n={n}, x={x}. Expected {expected}, got {result_dp}"
            print(f"DP Test passed for n={n}, x={x}. Result: {result_dp}")      


if __name__ == '__main__':
    test()