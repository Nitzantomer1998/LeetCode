def combine(number: int, k: int) -> list[list[int]]:
    """
    Creating all the possible combinations of k numbers chosen from the range [1, n], and return it

    :param number: Integer representing the highest digit value allowed
    :param k: Integer representing the permutation needed length
    :return: All the possible combinations

    Time Complexity: o(nCk)
    Space Complexity: o(n * k)
    """
    # Constants for the max possible digit value, and the permutation length, for more readable code
    MAX_VALUE = number + 1
    PERMUTATION_LENGTH = k

    # List to store all the possible permutation
    permutation_solution = []

    # Assisting function to make the DFS calls
    def add_nth_permutation(current_digit: int, current_permutation: list[int]) -> None:
        """
        Adding all the possible permutation that start with the current_digit

        :param current_digit: Integer representing the starting value of a permutation
        :param current_permutation: List Representing the current built permutation
        :return: Nothing, everything happens in place
        """
        # if we have built possible permutation, add permutation to solution and end call
        if len(current_permutation) == PERMUTATION_LENGTH:
            permutation_solution.append(current_permutation)
            return

        # if we haven't finished to build a permutation, make callback for each possible next digit
        for next_digit in range(current_digit + 1, MAX_VALUE):
            add_nth_permutation(next_digit, current_permutation + [next_digit])

    # Making callback for each digit till max number, which will add the possible permutations starting with the digit
    for digit in range(1, MAX_VALUE):
        add_nth_permutation(digit, [digit])

    # Returning the built solution
    return permutation_solution
