def num_trees(n: int) -> int:
    """
    Returns the number of structurally unique BSTs that can be formed using n nodes with values from 1 to n.

    :param n: The number of nodes.
    :return: The number of structurally unique BSTs.

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # calculate n-th Catalan number using formula
    catalan = 1
    for i in range(n):
        # calculate (2n)!
        catalan *= 2 * (2 * i + 1)
        # calculate (n+1)!
        catalan //= (i + 2)

    # Return the number of structurally unique BSTs
    return catalan
