#!/usr/bin/env python3
def divisors(n):
    # Write your code here
    count = 0
    for j in range(2, n//2 +1, 2):
        if n % j == 0 and j % 2 == 0    :
            count += 1

    return count


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = divisors(num)
    if result:
        print(f"Number of even divisors of {num} is {result}.")
    else:
        print(f"{num} has no even divisors.")