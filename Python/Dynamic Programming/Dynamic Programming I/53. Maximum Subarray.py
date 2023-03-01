def max_sub_array(numbers: list[int]) -> int:
    """
    Find the subarray with the largest sum, and return it

    :param numbers: List of integers
    :return: The subarray with the largest sum

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Loop to traverse each cell in numbers from end to start
    for index in range(len(numbers) - 2, -1, -1):

        # Updating the current index value because adding the value from his right (sequence) enlarging him
        if numbers[index] + numbers[index + 1] > numbers[index]:
            numbers[index] += numbers[index + 1]

    # Returning the maximum numbers in numbers, after we update each cell to be his highest possible
    return max(numbers)
