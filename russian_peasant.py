import math

'''
Exponentian using Russian Peasant's method.
This method is efficient for calculating large powers modulo a number.
It works by repeatedly squaring the base and reducing the exponent by half.

The algorithm is based on the principle that:
- If the exponent is even, then a^b = (a^(b/2))^2
- If the exponent is odd, then a^b = a * (a^(b-1))

This method reduces the number of multiplications needed to compute large powers.

This implementation exponentiates complex numbers.

'''

def russian_peasant(base: complex, exponent: int, mod: int) -> complex:
    """
    Calculate (base^exponent) % mod using Russian Peasant's method.
    
    :param base: The base number (can be complex)
    :param exponent: The exponent (integer)
    :param mod: The modulus (integer)
    :return: The result of (base^exponent) % mod
    """
    if mod == 1:
        return 0  # Any number mod 1 is 0
    
    result = 1
    base = base
    
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result = (result * base)
            result = complex(result.real % mod, result.imag % mod)
        exponent //= 2
        base = (base * base)
        base = complex(base.real % mod, base.imag % mod)  # Ensure base is within mod
    
    result = complex(result.real % mod, result.imag % mod)
        
    return result

def main():
    """
    Main function to test the russian_peasant function with sample input.
    """
    # Example usage
    base = complex(2, 3)  # 2 + 3i
    exponent = 5
    mod = 1000
    result = russian_peasant(base, exponent, mod)
    print(f"Result of ({base} ^ {exponent}) % {mod} is: {result}")

if __name__ == "__main__":
    main()
              