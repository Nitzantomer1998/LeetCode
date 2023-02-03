def single_number(numbers: list[int]) -> int:
    """
    Finding the unique element in am array which every element appears twice except for one. and return it.

    :param numbers: List of integers
    :return: The unique number

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable to store the solution
    single_number_solution = 0

    # Loop to traverse all the numbers
    for value in numbers:
        # Update the single number solution by making XOR operator with all the available numbers
        # Note : XOR operator return 1 only if the two bits values are difference, else it will be 0
        # Therefor only when we hit the True single number, the bits wouldn't change till we finished
        single_number_solution ^= value

    # Return the single number solution
    return single_number_solution
