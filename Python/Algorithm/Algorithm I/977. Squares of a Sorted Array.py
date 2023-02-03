def sorted_squares(numbers: list[int]) -> list[int]:
    """
    Creating array of the squares of each number sorted in non-decreasing order, and return it

    :param numbers: List of integers, sorted by ascending order
    :return: The sorted array after it has been squared

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # List to store the solution
    sorted_squares_solution = []

    # Left & Right, pointer to the Start & End of the array
    left, right = 0, len(numbers) - 1

    # Loop to traverse numbers without repeating
    while left <= right:

        # if the value on the left side is bigger
        if abs(numbers[left]) > abs(numbers[right]):

            # Add the bigger value to the solution
            sorted_squares_solution.append(numbers[left] ** 2)

            # Update the left pointer
            left += 1

        # if the value of the right side is bigger
        else:

            # Add the bigger value to the solution
            sorted_squares_solution.append(numbers[right] ** 2)

            # Update the right pointer
            right -= 1

    # Returning the solution
    return sorted_squares_solution[::-1]
