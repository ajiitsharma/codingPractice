class Solution:
    def fast_exponent(self, x: float, n: int) -> float:

        m = abs(n)
        base, result = x, 1

        while m:
            if m % 2 != 0:
                result = result * base

            base *= base
            m //=2

        if n < 0:
            result = 1/result
        
        return result
    
if __name__ == '__main__':
    solution = Solution()
    test_cases = [(2,10), (4, 50), (2,-10)]
    for case in test_cases:
        res = solution.fast_exponent(case[0], case[1])
        print(f'{case[0]}^{case[1]} ={res}')