def range_bitwise_and(left: int, right: int) -> int:
    """
    Finding the bitwise AND of all numbers in the range [left, right], and return it

    :param left: Integer represent the left boundary
    :param right: Integer represent the right boundary
    :return: The bitwise AND of all numbers in the range [left, right]

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Integer counter for the amount of rotate shift right we did
    shift_right_counter = 0

    # Loop which run till the bits are the same
    while left != right:
        # Shifting right for the next iteration
        left >>= 1
        right >>= 1

        # Updating the shift right rotate counter
        shift_right_counter += 1

    # Returning the bitwise AND of all numbers in the range [left, right]
    return left << shift_right_counter
