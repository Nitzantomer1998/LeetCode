def move_zeroes(numbers: list[int]) -> None:
    """
    Update numbers by moving all zero's to the end, while maintaining relative order of the non-zero elements
    :param numbers: List of integers
    :return: None, Everything happen in place

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Left & Next Left pointers, Left for the start index swap, and next left for the end index swap
    left, next_left = 0, 1

    # Loop to traverse every index in numbers
    while next_left < len(numbers):

        # Simple case, current index needed to be swapped with the next index
        if numbers[left] == 0 and numbers[next_left] != 0:
            numbers[left], numbers[next_left] = numbers[next_left], numbers[left]

            # Update pointers for the next iteration
            left += 1
            next_left += 1

        # Both of the indices are zero, therefor we need to update only the second index
        elif numbers[left] == 0 and numbers[next_left] == 0:
            next_left += 1

        # Current index doesn't need to be taken care of, then update both of the pointers
        else:
            left += 1
            next_left += 1

    # Explicit None return, everything happen in place nothing need to be return
    return
