'''
        There are N stacks of plates
        Each stack contains K plates
        Each plate has a beauty score

        Objective is to maxismize the score in collecting P plates
        Constraints: if you want to take the jth plate in a stack you have to take all plates from 0 to j in that stack
'''

import math

class PlateStack():

        def __init__(self, stack_count: int, stack_size: int, stack: list[list[int]]) -> None:
                self.stack_count = stack_count
                self.stack_size = stack_size
                self.stack = stack

        def _stack_sum(self) -> None:
                stack_verticle_score = []
                for j in range(self.stack_count):
                        _csum = 0
                        _csum_array = []
                        for val in self.stack[j]:
                                _csum += val
                                _csum_array.append(_csum)

                        stack_verticle_score.append(_csum_array)

                self.stack_verticle_score = stack_verticle_score

        def get_max_score(self, target: int) -> int:

                if target == 0:
                        return 0

                if self.stack_count * self.stack_size < target:
                        return -1

                dp = [[0] * self.stack_count for _ in range(target + 1)]
                self._stack_sum()

                # base case for first stack, with only one stack pick from the top
                for p in range(1, min(target, self.stack_size) + 1):
                        dp[p][0] = self.stack_verticle_score[0][p - 1]

                # base case when there is just 1 plate to select
                for s in range(1, self.stack_count):
                        dp[1][s] = max(dp[1][s - 1], self.stack[s][0])

                # dp for remaining stacks
                for p in range(2, target + 1):
                        for s in range(1, self.stack_count):

                                _bestk = dp[p][s - 1] # no items from sth stack

                                # now compare with taking k from sth stack and p - k from stacks till s - 1
                                max_k = min(p, self.stack_size)
                                for k in range(1, max_k):
                                        _bestk = max(_bestk, dp[p - k][s - 1] + self.stack_verticle_score[s][k - 1])

                                dp[p][s] = _bestk

                return dp[target][self.stack_count - 1]



if __name__ == '__main__':
        case_count = int(input('Enter the number of cases to test: '))

        for j in range(case_count):
                print(f'Case {j}')
                N, K, P = list(map(int, input('Enter number of plate stacks, number of plates in each stack and number of plates to collect: ').strip().split()))

                stack = [[0]*K for _ in range(N)]
                for i in range(N):
                        stack[i] = list(map(int, input(f'Enter the beauty scores of stack {i+1}: ').strip().split()))

                solution = PlateStack(N, K, stack)
                max_score = solution.get_max_score(P)

                print(f'Max beauty score = {max_score}')
