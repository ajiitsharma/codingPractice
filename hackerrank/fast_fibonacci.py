import math

'''
Fast Fibonacci calculation using matrix exponentiation.
This method computes Fibonacci numbers in O(log n) time complexity.
'''


def mat_mult(a, b):
    """Multiply two 2x2 matrices."""
    return [
        [a[0][0]*b[0][0] + a[0][1]*b[1][0],
         a[0][0]*b[0][1] + a[0][1]*b[1][1]],
        [a[1][0]*b[0][0] + a[1][1]*b[1][0],
         a[1][0]*b[0][1] + a[1][1]*b[1][1]]
    ]

def mat_pow(mat, n):
    """Raise a 2x2 matrix to the power n using fast exponentiation."""
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = mat_mult(result, mat)
        mat = mat_mult(mat, mat)
        n //= 2
    return result

def fast_fibonacci(n):
    """Compute the nth Fibonacci number using matrix exponentiation."""
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = mat_pow(base, n-1)
    return result[0][0]

if __name__ == '__main__':
    # Test cases for fast Fibonacci
    for i in range(100, 1000, 100):
        print(f"F({i}) =", fast_fibonacci(i))


