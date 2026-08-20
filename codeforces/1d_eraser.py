'''
You are given a strip of paper s that is n cells long. Each cell is either black or white. 
In an operation you can take any k consecutive cells and make them all white.

Find the minimum number of operations needed to remove all black cells
'''

def min_edits(string: str, window: int, size: int) -> int:
        count = 0
        j = 0
        while j < size:
                if string[j] == 'W':
                        j += 1
                elif string[j] == 'B':
                        count += 1
                        j += window
        return count

if __name__ == '__main__':
        cases = int(input())
        for _ in range(cases):
                size, window = map(int, input().strip().split())
                string = str(input().strip())

                result = min_edits(string, window, size)
                print(result)

