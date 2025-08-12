import math

'''
How many rocks can appear at locations (x,y) on the line segment between P1 and P2 (excluding P1 and P2) which satisfy the condition that both x and y are integers?
This is equivalent to finding the number of integer points on the line segment between two points P1 and P2 in a 2D plane.
The line segment is defined by the two points P1(x1, y1) and P2(x2, y2).
The number of integer points on the line segment can be calculated using the formula:
gcd(abs(x2 - x1), abs(y2 - y1)) - 1
This gives the count of integer points excluding the endpoints.
'''

def integer_points_on_line(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Calculate the number of integer points on the line segment between two points P1 and P2.
    
    :param x1: x-coordinate of point P1
    :param y1: y-coordinate of point P1
    :param x2: x-coordinate of point P2
    :param y2: y-coordinate of point P2
    :return: Number of integer points on the line segment excluding endpoints
    """
    return math.gcd(abs(x2 - x1), abs(y2 - y1)) - 1     

def main():
    """
    Main function to test the integer_points_on_line function with sample input.
    """
    # Example usage
    x1, y1 = 1, 2
    x2, y2 = 4, 6
    result = integer_points_on_line(x1, y1, x2, y2)
    print(f"Number of integer points on the line segment between ({x1}, {y1}) and ({x2}, {y2}): {result}")

if __name__ == "__main__":
        main()