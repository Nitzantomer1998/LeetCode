def min_sub_array_len(target: int, numbers: list[int]) -> int:
    """
    Finding the minimal length of a subarray whose sum is greater than or equal to target, and return it
    Note : if the summation of all the list still lower than target, return 0

    :param numbers: List of integers
    :param target: Integer representing the summation target
    :return: The minimal length of a subarray whose sum is greater than or equal to target if found, else 0

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Integer storing the solution of the minimum needed sub-array length that their sum is greater equal to target
    min_subarray_solution = len(numbers) + 1

    # Start pointer representing the start of the current window
    start_index = 0

    # Integer storing the current summation value
    current_sum = 0

    # Loop to traverse numbers list
    # Note : end_index represent the end of the current window
    for end_index, value in enumerate(numbers):

        # Updating the summation of the current iteration
        current_sum += value

        # Loop to fix the current window in case the total sum is greater equal to target
        while current_sum >= target and start_index <= end_index:
            # Update the solution to be the minimum length
            min_subarray_solution = min(min_subarray_solution, end_index - start_index + 1)

            # Update the new window summation, and starting point
            current_sum -= numbers[start_index]
            start_index += 1

    # Returning the min length of sub array with summation that greater equal to target if found, else 0
    return min_subarray_solution if min_subarray_solution <= len(numbers) else 0
