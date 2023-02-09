def permute_unique(numbers: list[int]) -> list[list[int]]:
    """
    Creating all the possible permutations out of numbers without duplicates, and return it

    :param numbers: List of integers
    :return: All the possible permutations out of numbers without duplicates

    Time Complexity: o(n * n!)
    Space Complexity: o(n * n!)
    """
    # List storing all the possible permutation
    permute_solution = []

    # Sorting numbers
    numbers.sort()

    # Assisting function to make the DFS calls
    def add_permute(numbers: list[int], current_permute: list[int]) -> None:
        """
        Adding all the possible permutation that start with the current_digit

        :param numbers: List filled with digits we yet used for the current permutation
        :param current_permute: List Representing the current built permutation
        :return: Nothing, everything happens in place
        """
        # if we have built full permutation, add permutation to solution and end call
        if not numbers:
            permute_solution.append(current_permute)
            return

        # if we haven't finished to build a permutation, make callback for each possible next digit
        for index in range(len(numbers)):

            # if statement to avoid permutation duplicates
            if index > 0 and numbers[index] == numbers[index - 1]:
                continue

            add_permute(numbers[:index] + numbers[index + 1:], current_permute + [numbers[index]])

    # Making the first callback which will create all the needed callbacks until we found all the unique permutations
    add_permute(numbers, [])

    # Returning all the possible unique permutations
    return permute_solution
