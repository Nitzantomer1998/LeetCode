def num_squares(n: int) -> int:
    """
    Find the least number of perfect squares that sum to n, and return it

    :param n: An integer
    :return: The least number of perfect squares that sum to n.

    Time Complexity: o(n * sqrt(n))
    Space Complexity: o(n)
    """
    # Create a list of squares less than or equal to n
    squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

    # Initialize a list of counts with n + 1, since we can have at most n 1's
    counts = [n + 1] * (n + 1)

    # There is one way to form 0
    counts[0] = 0

    # Iterate over all possible numbers from 1 to n
    for i in range(1, n + 1):

        # Iterate over all squares that are less than or equal to i
        for square in squares:

            # If the square is greater than i, we cannot use it
            if square > i:
                break

            # Update the count for the current number i
            counts[i] = min(counts[i], counts[i - square] + 1)

    # The least number of perfect squares that sum to n is stored in counts[n]
    return counts[n]
