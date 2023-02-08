def subsets(numbers: list[int]) -> list[list[int]]:
    """
    Finding all the possible subset in numbers, and return it

    :param numbers: List of integers
    :return: All the possible subset in numbers

    Time Complexity: o(n * 2 ^ n)
    Space Complexity: o(n * 2 ^ n)
    """
    # List storing all the possible subsets
    subsets_solution = []

    # Assisting function to make the DFS calls
    def add_subset(index: int, current_subset: list[int]) -> None:
        """
        Adding all the possible subsets in numbers

        :param index: Integer representing the current index in numbers
        :param current_subset: List representing the current subset
        :return: Nothing, everything happens in place
        """
        # Adding the current subset to the solution
        subsets_solution.append(current_subset)

        # Loop that's makes a callback for each subset possibility with updating the current subset
        for next_index in range(index, len(numbers)):
            add_subset(next_index + 1, current_subset + [numbers[next_index]])

    # Making the first callback that will create all the needed callbacks for the solution
    add_subset(0, [])

    # Returning all the possible subsets in numbers
    return subsets_solution
