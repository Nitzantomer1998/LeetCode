def jump(numbers: list[int]) -> int:
    """
    Finding the minimum numbers of jumps needed to reach to the last index, starting from cell 0, and return it
    Note : Each value in numbers represent the maximum jump he can make from there

    :param numbers: List of integers
    :return: The minimum numbers of jumps needed to reach to the last index, starting from cell 0

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Integer storing the minimum needed jumps to reach to the last index
    min_jumps_made = 0

    # Left & Right pointers, used for enhances bfs algorithm, [left, right] indices are on the same level
    left = right = 0

    # Loop to traverse each "level" in numbers
    while right < len(numbers) - 1:
        # Integer storing the farthest possible index we can get from the current level
        farthest = 0

        # Loop traversing the indices in the current level, and updating farthest to be the maximum possible jump
        for index in range(left, right + 1):
            farthest = max(farthest, index + numbers[index])

        # Updating the pointers to point on the next level, and the jump counter
        left = right + 1
        right = farthest
        min_jumps_made += 1

    # Returning the minimum jumps made
    return min_jumps_made
