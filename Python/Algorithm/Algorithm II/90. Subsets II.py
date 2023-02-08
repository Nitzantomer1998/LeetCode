def subsets_with_dup(numbers: list[int]) -> list[list[int]]:
    """
    Finding all the possible subset in numbers without duplicates, and return it

    :param numbers: List of integers
    :return: All the possible subset in numbers without duplicates

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n)
    """
    # List storing all the possible subsets
    subsets_solution = [[]]

    # Sorting numbers
    numbers.sort()

    # Integer storing the previous subsets solution amount
    previous_subsets_size = 0

    # Loop to traverse each index in numbers
    for i in range(len(numbers)):

        # Start index is a pointer to the starting cell
        start_index = previous_subsets_size if i > 0 and numbers[i] == numbers[i - 1] else 0

        # Updating the previous subsets solution amount
        previous_subsets_size = len(subsets_solution)

        # Loop for adding all the possible subsets for the current cell
        for j in range(start_index, previous_subsets_size):
            subsets_solution.append(subsets_solution[j] + [numbers[i]])

    # Returning all the possible subsets in numbers
    return subsets_solution
