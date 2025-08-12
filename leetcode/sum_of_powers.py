class Solution:
    
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
        
        return count

def main():
    """
    Main function to test the numberOfWays function with sample input.
    """
    # Example usage
    n = [4, 10, 27, 100, 1000, 1000]
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
            
if __name__ == '__main__':
    main()