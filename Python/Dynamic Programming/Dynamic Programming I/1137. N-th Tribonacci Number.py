def tribonacci(n: int) -> int:
    """
    Find the value of tribonacci(n), and return it
    Note: t(0) = 0, t(1) = 1, t(2) = 1, and the rules are t(n) = t(n - 1) + t(n - 2) + t(n - 3)

    :param n: Integer representing the index in the tribonacci tree
    :return: The value of tribonacci(n)

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # List storing the previous and current and next tribonacci values
    tri = [0, 1, 1]

    # Loop to build the tribonacci numbers
    for _ in range(n - 2):
        # In each iteration calculate the next tribonacci number, and update accordingly
        tri[0], tri[1], tri[2] = tri[1], tri[2], sum(tri)

    # Returning the tribonacci solution
    return tri[n] if n < 3 else tri[-1]
