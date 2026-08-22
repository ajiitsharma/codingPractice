'''
        https://codeforces.com/contest/2257/problem/B

        Beaver war

        Approach: Whoever is at greater options will have more bandwidth to take hit
        This options depends upon the max height (as he jump when he encounter a stack higher than his current stack)
                and number of horizontal jumps he can can which equals the total numbe rof stack he has
'''
def solve(arrA: list[int], A: int, arrB: list[int], B: int) -> int:
        '''
        Returns 1 if A wins or 2 if B wins
        '''

        options_A = A + max(arrA)
        options_B = B + max(arrB)

        if options_A >= options_B:
                return 1
        else:
                return 2

if __name__ == '__main__':
        N = int(input())

        for _ in range(N):
                A, B = list(map(int, input().strip().split()))
                heights_A = list(map(int, input().strip().split()))
                heights_B = list(map(int, input().strip().split()))
                result = solve(heights_A, A, heights_B, B)

                print(result)