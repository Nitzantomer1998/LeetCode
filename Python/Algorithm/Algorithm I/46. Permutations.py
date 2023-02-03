def permute(numbers: list[int]) -> list[list[int]]:
    """
    Creating all the possible permutations out of numbers, and return it

    :param numbers: List of integers
    :return: All the possible permutations out of numbers

    Time Complexity: o(n * n!)
    Space Complexity: o(n * n!)
    """
    # List to store all the possible permutation
    permute_solution = []

    # Assisting function to make the DFS calls
    def add_permute(current_permute: list[int], digits_left: list[int]) -> None:
        """
        Adding all the possible permutation that start with the current_digit

        :param current_permute: List Representing the current built permutation
        :param digits_left: List filled with digits we yet used for the current permutation
        :return: Nothing, everything happens in place
        """
        # if we have built full permutation, add permutation to solution and end call
        if len(digits_left) == 0:
            permute_solution.append(current_permute)
            return

        # if we haven't finished to build a permutation, make callback for each possible next digit
        for next_digit in digits_left:
            # Making the callback for the next step for the permutation, with updating the left needed digits
            add_permute(current_permute + [next_digit], [digit for digit in digits_left if digit != next_digit])

    # Making callback for each digit in numbers, which will add the possible permutations starting with the digit
    for digit in numbers:
        add_permute([digit], [value for value in numbers if value != digit])

    # Returning the built solution
    return permute_solution
