import math
from functools import wraps
import time


def compute_max_rod_cut_value_memo(size: int, prices: list[int], memo: dict = None) -> tuple[int, list[list[int]]]:

        if memo is None:
                memo = {}

        if size == 0:
                return (0,[[]])

        if size == 1:
                memo[size] = (prices[0], [[size]])
                return memo[size]

        if size in memo:
                return memo[size]
        
        max_value = 0
        max_single_cut = min(size, len(prices))

        combinations = []

        for j in range(1, max_single_cut + 1):
                left_cut = prices[j-1]
                right_cut, right_combination = compute_max_rod_cut_value_memo(size - j, prices, memo)

                curr_value = left_cut + right_cut
                max_value = max(max_value, curr_value)

                for row in right_combination:
                        combinations.append(([j] + row, curr_value))

        # remove duplicates
        unique_combinations = set()
        for comb, val in combinations:
                if val == max_value:
                        unique_combinations.add(tuple(sorted(comb)))


        best_combination = [list(comb) for comb in unique_combinations]

        memo[size] = (max_value, best_combination)

        return (max_value, best_combination)



def compute_max_rod_cut_value(size: int, prices: list[int]) -> int:

        if size == 0:
                return 0

        if size == 1:
                return prices[0]
        
        max_value = 0
        max_single_cut = min(size, len(prices))

        combinations = []

        for j in range(1, max_single_cut + 1):
                max_value = max(max_value, prices[j-1] + compute_max_rod_cut_value(size - j, prices))
                combinations.append([j, size - j, max_value])

        print(f'Combination for size: {size}')
        for comb in combinations:
                print(f'Split = {comb[0]} + {comb[1]} :: Value = ₹ {comb[2]}')
        return max_value

if __name__ == '__main__':
        prices = [1, 5, 8, 9, 10, 17, 17, 20]        # first element is always 0 as value of size 0 = 0
        size = 20

        # result = compute_max_rod_cut_value(size, prices)
        result = compute_max_rod_cut_value_memo(size, prices)

        print(f'Max value = ₹{result[0]} with the combinations:')
        for row in result[1]:
                print(row)
