def generate_parenthesis(n: int) -> list[str]:
    """
    Finding all the well-formed parenthesis pairs permutation, and return it

    :param n: Integer represent the amount of parenthesis pairs needed
    :return: All the well-formed parenthesis pairs permutation

    Time Complexity: o(2 ^ n)
    Space Complexity: o(2 ^ n)
    """
    # List storing all the allowed combinations of parenthesis
    parenthesis_solution = []

    # Assisting function to make the backtracking calls
    def add_permutation(open_parenthesis: int, close_parenthesis: int, current_permutation: list[str]) -> None:
        """
        Adding all the possible combinations that start with the index using DFS algorithm

        :param open_parenthesis: Integer represent the amount of open parenthesis
        :param close_parenthesis: Integer represent the amount of close parenthesis
        :param current_permutation: List Representing the current built permutation
        :return: Nothing, everything happens in place
        """
        # if all of those parameters are equals, we have created full permutation, add it to the solution and return
        if open_parenthesis == close_parenthesis == n:
            parenthesis_solution.append(''.join(current_permutation))
            return

        # if open_parenthesis is smaller than n, than we may add another open parenthesis to the current permutation
        if open_parenthesis < n:
            add_permutation(open_parenthesis + 1, close_parenthesis, current_permutation + ['('])

        # if close is smaller than open, than we may add another close parenthesis to the current permutation
        if close_parenthesis < open_parenthesis:
            add_permutation(open_parenthesis, close_parenthesis + 1, current_permutation + [')'])

    # Making the first callback which will create all the needed callbacks until we found all the unique permutations
    add_permutation(0, 0, [])

    # Returning all the well-formed parenthesis pairs permutation
    return parenthesis_solution
