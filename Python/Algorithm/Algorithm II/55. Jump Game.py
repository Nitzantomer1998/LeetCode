def can_jump(numbers: list[int]) -> bool:
    """
    Finding if we can jump to the last cell in numbers, starting from cell 0, and return accordingly
    Note : Each value in numbers represent the maximum jump he can make from there

    :param numbers: List of integers
    :return: True if we can jump to the last cell in numbers from start, else False

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Integer storing the minimum index for succeeding the goal
    target_index = len(numbers) - 1

    # Loop to traverse each number in numbers (in reversed order)
    for index in range(len(numbers) - 1, -1, -1):

        # if we can get to target index, update it to be the new minimum index
        if index + numbers[index] >= target_index:
            target_index = index

    # Returning True if the target_index equal 0 because we can get to the goal from there, else False
    return True if target_index == 0 else False
