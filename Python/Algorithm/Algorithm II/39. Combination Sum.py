def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Creating all the unique combinations out of candidates which their sum equal to target, and return it

    :param candidates: List of integers
    :param target: Integer represent the goal for a combination to achieve
    :return: All the unique combinations out of candidates which their sum equal to target

    Time Complexity: o(n * n!)
    Space Complexity: o(n * n!)
    """
    # List storing all the unique combinations that equal to target
    combinations_solution = []

    # Assisting function to make the DFS calls
    def add_combination(index: int, current_sum: int, current_combination: list[int]) -> None:
        """
        Adding all the possible combinations that start with the index using DFS algorithm

        :param index: Integer represent the current index in candidates
        :param current_sum: Integer represent the current sum of the built current combination
        :param current_combination: List Representing the current built combination
        :return: Nothing, everything happens in place
        """
        # if we found combination that equals to target, add it to the solution and end call
        if current_sum == target:
            combinations_solution.append(current_combination)
            return

        # if the current combination sum is greater than target, than its failed, end call
        elif current_sum > target:
            return

        # if we haven't finished to build a combination, make callback for each possible next digit
        for i in range(index, len(candidates)):
            add_combination(i, current_sum + candidates[i], current_combination + [candidates[i]])

    # Making the first callback which will create all the needed callbacks until we found all the unique permutations
    add_combination(0, 0, [])

    # Returning all the unique solution combinations
    return combinations_solution
