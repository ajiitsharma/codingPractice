#!/usr/bin/env python3



if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = highest_even_divisor(num)
    if result:
        print(f"The highest even divisor of {num} is {result}.")
    else:
        print(f"{num} has no even divisors.")