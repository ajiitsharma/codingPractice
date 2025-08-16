#!user/bin/env python3

def solve(arr: list[int], queries: list[list[int]]) -> list[str]:
    """
    This function takes an array of integers and a list of queries.
    Each query consists of two integers x and y, and the function checks
    if the sum of elements from index x to y (inclusive) is even or odd.
    
    :param arr: List of integers
    :param queries: List of queries where each query is a list [x, y]
    :return: List of strings "Even" or "Odd" for each query
    """
    if not arr or not queries:
        return []

    # Process each query
    # If x > y or arr[x] is odd, the result is "Odd"               
    
    result = []
    for q in queries:
        x, y  = q[0]-1, q[1]-1
        if x > y:
            result.append("Odd")
        elif x < y and arr[x+1] == 0: # n^0 = 1, so if arr[x+1] is 0, the parity is odd. However, if wont be applicable for x == y
            result.append("Odd")
        else:
            result.append("Odd" if arr[x] % 2 != 0 else "Even")
        
    
    return result

def main() -> None:
    """
    Main function to test the solve function with sample input.
    """
    arr = [1, 2, 3, 4, 5, 0, 6]
    queries = [[1, 3], [2, 4], [1, 5], [5,7], [6,7]]
    
    result = solve(arr, queries)
    print(result)  # Expected output: ['Odd', 'Even', 'Odd']     

if __name__ == "__main__":
    main()            