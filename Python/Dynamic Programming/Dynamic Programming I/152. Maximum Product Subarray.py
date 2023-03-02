def max_product(numbers: list[int]) -> int:
    """
    Find the largest subarray product, and return it

    :param numbers: List of integers
    :return: The largest subarray product

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variables storing the outcome values of the current product
    current_max, current_min = 1, 1

    # Integer storing the max product we found
    result = numbers[0]

    # Loop to traverse each number in numbers
    for value in numbers:
        # Enumerate the possible values for the current cell
        values = (value, value * current_max, value * current_min)

        # Updating the max and min values to fit to the right variables
        current_max, current_min = max(values), min(values)

        # Updating the max product value
        result = max(result, current_max)

    # Returning the max found subarray product
    return result
