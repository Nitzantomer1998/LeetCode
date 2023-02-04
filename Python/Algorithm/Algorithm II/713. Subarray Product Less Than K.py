def num_subarray_product_less_than_k(numbers: list[int], k: int) -> int:
    """
    Finding the amount of contiguous sub-arrays that less than k in numbers, and return it

    :param numbers: List of integers
    :param k: Integer representing the max value of contiguous
    :return: The amount of contiguous sub-arrays that less than k in numbers

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Integer storing the solution counter of existing sub-arrays contiguous that less than k
    subarray_solution_counter = 0

    # Start pointer representing the start of the current window
    start_index = 0

    # Integer storing the current multiplication value
    current_sum = 1

    # Loop to traverse numbers list
    # Note : end_index represent the end of the current window
    for end_index, value in enumerate(numbers):

        # Updating the multiplication sum of the current iteration
        current_sum *= value

        # Loop to fix the current window in case the total sum is greater equal to k
        while current_sum >= k and start_index <= end_index:
            current_sum /= numbers[start_index]
            start_index += 1

        # Updating the solution counter according the current iteration
        subarray_solution_counter += (end_index - start_index + 1)

    # Returning the amount of contiguous sub-arrays that less than k in numbers
    return subarray_solution_counter
