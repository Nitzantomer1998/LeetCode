def letter_case_permutation(string: str) -> list[str]:
    """
    Creating all the possible permutation by swapping lower / upper case characters, and return it

    :param string: String
    :return: All the possible permutation by swapping lower / upper case characters

    Time Complexity: o(2^n)
    Space Complexity: o(n)
    """
    # List to store all the possible permutations
    permutation_solution = []

    # Assisting function to make the DFS calls
    def add_permutation(index: int, current_list: list[str]) -> None:
        """
        Adding the possible permutation for the current index

        :param index: Integer representing the char we are at
        :param current_list: List Representing the current built permutation
        :return: Nothing, everything happens in place
        """
        # if we have built possible permutation, add permutation to solution and end call
        if index == len(string):
            permutation_solution.append(''.join(current_list))
            return

        # if we haven't finished to build a permutation, and we hit an integer, make callback for the next character
        if '0' <= string[index] <= '9':
            add_permutation(index + 1, current_list + [string[index]])

        # if we haven't finished to build a permutation, and we hit a char, make 2 callback with lower and upper case
        else:
            add_permutation(index + 1, current_list + [string[index]])
            add_permutation(index + 1, current_list + [string[index].swapcase()])

    # Activating the recursive DFS in order to get all the possible permutations
    add_permutation(0, [])

    # Returning all the possible permutations
    return permutation_solution
