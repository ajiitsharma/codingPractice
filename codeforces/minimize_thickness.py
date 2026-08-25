'''
        https://codeforces.com/problemset/problem/1741/C

        Approach:
                if there are n elements in the array, there can be at max n - 1 partitions, min = 1
                creating n blocks
                S = sum of array
                If each block has to have equal sum then block_sum = S / (partitions + 1)

                To check a valid partition,
                        get cumsum array
                        count of cumsum[j] % block_sum must equal (partition + 1)

'''
import math

def get_min_partition_order(nums: list[int], N: int) -> int:

        # get cummulative sum and total sum S
        cumsum = []
        S = 0
        for num in nums:
                S += num
                cumsum.append(S)

        # using a set for O(1) prefix lookup
        cumsum_set = set(cumsum)

        min_order = N
        for partitions in range(1, N):
                num_blocks = partitions + 1

                if S % num_blocks != 0:
                        continue

                block_sum = S // num_blocks

                target_multiples = [ i * block_sum for i in range(1, num_blocks + 1)]

                # all the target multiple must be in the set
                if all(target in cumsum_set for target in target_multiples):
                        # this partition is valid

                        # find the order using location of multiples
                        indices = [cumsum.index(target) for target in target_multiples]

                        # initialize first index at -1 for firts segment
                        prev_idx = -1 
                        max_thickness = 0

                        for idx in indices:
                                max_thickness = max(max_thickness, idx - prev_idx)
                                prev_idx = idx

                        # update min_order for this valid partition
                        min_order = min(min_order, max_thickness)

        return min_order


if __name__ == '__main__':
        T = int(input())
        for _ in range(T):
                N = int(input())
                nums = list(map(int, input().strip().split()))

                result = get_min_partition_order(nums, N)
                print(result)