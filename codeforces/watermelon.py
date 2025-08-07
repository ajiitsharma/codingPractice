
def watermelon(w: int) -> str:
    """
    Determine if a watermelon can be split into two even parts.
    
    :param w: Weight of the watermelon
    :return: "YES" if it can be split, "NO" otherwise
    """
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    w = int(input().strip())
    print(watermelon(w))