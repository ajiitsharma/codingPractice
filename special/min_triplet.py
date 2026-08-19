'''
        Given 3 sorted arrays, find the triplet (a, b, c) such that the max difference between the elements is minimum

        Approach: 
                Use 3 pointers i, j, k - one for each array
                find the min and max of the currect triplet selection
                increment the index of the minimum element
'''

def find_smallest_difference_triplet(A: list[int], B: list[int], C: list[int]) -> tuple[int, list[int]]:
        i, j, k = 0, 0, 0
        min_diff = float('inf')
        best_triplet = []

        while i < len(A) and j < len(B) and k < len(C):
                a, b, c = A[i], B[j], C[k]
                curr_max = max(a, b, c)
                curr_min = min(a, b, c)
                curr_diff = curr_max - curr_min

                if curr_diff < min_diff:
                        min_diff = min(min_diff, curr_diff)
                        best_triplet = [a, b, c]

                if curr_min == a:
                        i += 1
                elif curr_min == b:
                        j += 1
                else:
                        k += 1

        return (min_diff, best_triplet)

if __name__ == '__main__':
        A = [20, 24, 100]
        B = [2, 19, 22, 79, 800]
        C = [10, 12, 23, 24, 119]

        result = find_smallest_difference_triplet(A, B, C)
        print(f'Smallest difference = {result[0]} for triplets {result[1]}')
