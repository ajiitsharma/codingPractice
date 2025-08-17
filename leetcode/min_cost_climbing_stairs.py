#! user/bin/env python3

'''
Problem: https://leetcode.com/problems/min-cost-climbing-stairs/description/

Let us track the total_cost to reach index j -> total_cost[j]
total_cost[j] = min(total_cost[j-1] + cost[j-1], total_cost[j-2] + cost[j-2])

Note: the target is to reach index N where last index is N-1
'''

def min_cost(cost: list[int]) -> int:
        #trivial case
        if len(cost) < 2:
                return 0
        
        target_index = len(cost) + 1
        
        total_cost = [0]*target_index
        for j in range(2, target_index):
                total_cost[j] = min(total_cost[j-1] + cost[j-1], total_cost[j-2] + cost[j-2])

        print(total_cost)
        return total_cost[-1]

def test() -> None:
        test_cases = [
                [10,15,20],
                [1,100,1,1,1,100,1,1,100,1]
        ]

        for case in test_cases:
                solution = min_cost(case)
                print(f'{solution}')

if __name__ == '__main__':
        test()