import math

'''
This module provides a function to compute the value at a given position in an infinite grid.
Grid starts at the bottom left corner (1, 1) and increases in both row and column directions.

.............

20 22 24 26 28

11 13 15 17 19

10 12 14 16 18

 1  3  5  7  9

 0  2  4  6  8
'''

def computeGridValue(row: int, col: int) -> int:
    """
    Compute the value at a given position in an infinite grid.
    
    :param row: Row index (1-based)
    :param col: Column index (1-based)
    :return: Value at the specified position
    """

    # Grid can be considered as a block of 2 rows defined by row index

    row_block = (row - 1) // 2
    target = (col - 1)*2 +1 if row % 2 == 0 else (col - 1)*2
    target += row_block * 10

    return target

if __name__ == '__main__':
    # Test cases
    print(computeGridValue(1, 1))  # Expected output: 0
    print(computeGridValue(1, 2))  # Expected output: 2
    print(computeGridValue(2, 1))  # Expected output: 1
    print(computeGridValue(2, 2))  # Expected output: 3
    print(computeGridValue(6, 3))  # Expected output: 25