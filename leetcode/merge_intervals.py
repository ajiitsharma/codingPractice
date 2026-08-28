'''
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''

def merge_intervals(interval: list[list[int]]) -> list[list[int]]:

        return [[]]


if __name__ == '__main__':
        case_count = int(input('Enter the number of cases to test: '))

        for j in range(case_count):
                print(f'Case {j + 1}')
                raw_input = input("Enter intervals: ").strip()

                # Strip outer brackets and format into individual pairs
                # e.g., "[[1,3],[2,6]]" -> "1,3],[2,6" -> splits on "],["
                cleaned = raw_input.strip()[2:-2]
                intervals = [[int(x) for x in item.split(',')] for item in cleaned.split('],[')]

                print(f"Parsed array: {intervals}")

                result = merge_intervals(intervals)
                print("Merged intervals:", result)


