def get_max_len(numbers: list[int]) -> int:
    """
    Find the maximum length of a subarray with positive product, and return it

    :param numbers: List of integers
    :return: The maximum length of a subarray with positive product

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Counters for each sub-array + maximum positive sub-array
    max_length = positive = negative = 0

    # Loop to traverse each number in numbers
    for number in numbers:

        # Number is zero -> Reset the sub-arrays
        if number == 0:
            positive = negative = 0

        # Positive number -> positive counter increment, and negative doesn't affect so increment by 1
        elif number > 0:
            positive += 1

            # if negative is 0, then it can't be affected
            negative = 0 if negative == 0 else negative + 1

        # Negative number -> subarray becomes -ve and -ve becomes +ve after adding the new value due to sign reversal
        else:
            positive, negative = 0 if negative == 0 else negative + 1, positive + 1

        # Updating max length
        max_length = max(max_length, positive)

    # Returning the maximum length of a subarray with positive product
    return max_length
