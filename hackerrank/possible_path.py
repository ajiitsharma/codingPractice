import math

'''
Function to check if a cordinate is within bounds given a start and end point.
This function uses a backtracking approach to explore all possible paths from the start to the end point.
It returns True if a path exists, otherwise returns False.
This is useful in scenarios where we need to find a path in a grid or a maze.
'''

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

def backtrack(curr: Point, end: Point, visited: set[Point]) -> bool:
    if curr == end:
        return True

    if curr in visited:
        return False

    visited.add(curr)

    # Define possible moves
    moves = [
        Point(curr.x + curr.y, curr.y), 
        Point(curr.y - curr.x, curr.y),
        Point(curr.x, curr.y + curr.x), 
        Point(curr.x, curr.x - curr.y)
        ]

    for move in moves:
        if backtrack(move, end, visited):
            return True

    visited.remove(curr)
    return False

def is_path_possible(start: Point, end: Point) -> bool:
    visited = set()
    return backtrack(start, end, visited)       

if __name__ == '__main__':
    # Example usage
    start = Point(1, 1)
    end = Point(2, 3)
    result = is_path_possible(start, end)
    print(f"Is path possible from {start} to {end}: {result}")
    # Expected output: True if a path exists, otherwise False
    
    start = Point(2, 1)
    end = Point(2, 3)
    result = is_path_possible(start, end)
    print(f"Is path possible from {start} to {end}: {result}")
    # Expected output: True if a path exists, otherwise False

    start = Point(3, 3)
    end = Point(1, 1)
    result = is_path_possible(start, end)
    print(f"Is path possible from {start} to {end}: {result}")
    # Expected output: True if a path exists, otherwise False
