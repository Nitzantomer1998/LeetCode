def search(numbers: list[int], target: int) -> int:
    """
    Searching the index of target in numbers, and return it if exist else -1

    :param numbers: List of integers sorted by ascending order
    :param target: Integer represent desire value in numbers
    :return: The index of target in numbers if exist else -1

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Pointers to current array we are searching at
    left, right = 0, len(numbers) - 1

    # Loop to traverse numbers without repeating
    while left <= right:

        # Variable to store the middle index of the current container we are searching at
        middle = (right + left) // 2

        # if we found the desire target, return its index
        if numbers[middle] == target:
            return middle

        # if numbers[middle] is bigger, than we narrow the container to be [left, middle - 1]
        elif numbers[middle] > target:
            right = middle - 1

        # if numbers[middle] is lower, than we narrow the container to be [middle + 1, right]
        else:
            left = middle + 1

    # if we reach here, then target isn't exist in numbers, return default value
    return -1
