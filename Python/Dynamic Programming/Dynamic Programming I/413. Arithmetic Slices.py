def number_of_arithmetic_slices(numbers: list[int]) -> int:
    """
    Finding the amount of arithmetic sub-arrays in numbers, and return it

    :param numbers: List of integers
    :return: The amount of arithmetic sub-arrays in numbers

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # List storing in the nth cell the amount of arithmetic series that end in that index
    nth_arithmetic_counter = [0] * len(numbers)

    # Loop to traverse each cell in numbers, starting from 2 because minimum arithmetic series is length of 3
    for index in range(2, len(numbers)):

        # if the current index, keep that arithmetic series fixed, update nth_arithmetic_counter
        if numbers[index] - numbers[index - 1] == numbers[index - 1] - numbers[index - 2]:
            nth_arithmetic_counter[index] = 1 + nth_arithmetic_counter[index - 1]

    # Retuning the arithmetic series amount by sum all the created list
    return sum(nth_arithmetic_counter)
