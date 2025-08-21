import math
from collections import Counter

def get_decimal(num: int, base: int) -> int:
        dec, j = 0, 0
        while num:
                last_digit = (num % 10)
                if last_digit >= base:
                        return -1
                dec +=  last_digit * base**j
                num //= 10
                j += 1
        return dec

def unique_pairs(dates: list[list[int]]) -> int:
        dec_numbers = [get_decimal(row[0], row[1]) for row in dates]
        counter = Counter(n for n in dec_numbers if n >= 0)

        total = 0
        for key, value in counter.items():
                total += value * (value-1) // 2
        
        return total

if __name__ == '__main__':
        dates = [[31,8],[25,10],[11001,2]]
        result = unique_pairs(dates)
        print(result)