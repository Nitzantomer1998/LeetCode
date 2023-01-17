def search_insert(numbers: list[int], target: int) -> int:
    """
    Searching for target in numbers, if exist return it index, else return its appropriate index to keep ascending order

    :param numbers: List of integers sorted by ascending order
    :param target: Integer represent desire value in numbers
    :return: The index of target in numbers if exist else its appropriate index to keep ascending order

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Variable to store the index solution
    insert_solution = 0

    # Pointers to current array we are searching at
    left, right = 0, len(numbers) - 1

    # Loop to traverse numbers without repeating
    while left <= right:

        # Variable to store the middle index of the current container we are searching at
        middle = (right + left) // 2

        # if we found the desire target, return its index
        if numbers[middle] == target:
            return middle

        # if numbers[middle] is bigger
        elif numbers[middle] > target:

            # Update the current possible insert solution
            insert_solution = middle

            # Narrow the container to be [left, middle - 1]
            right = middle - 1

        # if numbers[middle] is lower
        else:

            # Update the current possible insert solution
            insert_solution = middle + 1

            # Narrow the container to be [middle + 1, right]
            left = middle + 1

    # if we reach here, then target isn't exist in numbers, return the appropriate index
    return insert_solution
