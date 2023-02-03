def reverse_string(string: list[str]) -> None:
    """
    Update the list by reversing the sent string

    :param string: List of characters
    :return: None, Everything happen in place

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Pointers to the start and end of the string
    left, right = 0, len(string) - 1

    # Loop to traverse the list and update it
    while left < right:
        # Swapping characters position between the start and end indices
        string[left], string[right] = string[right], string[left]

        # Update the pointers, for the next iteration
        left += 1
        right -= 1

    # Explicit None return, everything happen in place nothing need to be return
    return None
