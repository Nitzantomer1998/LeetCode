def rob(numbers: list[int]) -> int:
    """
    Finding the maximum amount of money you can rob tonight without alerting the police, and return it
    Note : if you visit an adjacent the cops will show up
    Note : Numbers is a circle, meaning cell [0, n - 1] are adjacent

    :param numbers: List of integers Representing amount of money in each house
    :return: The maximum amount of money you can rob tonight without alerting the police

    Time Complexity: o(n)
    Space Complexity: o(1)
    """

    # Assisting function that calculate "rob" function without circles (DAG)
    def acyclic_rob(start_index: int, end_index: int) -> int:
        """
        Finding the maximum amount of money you can rob tonight without alerting the police, and return it
        Note : if you visit an adjacent the cops will show up

        :param start_index: Integer represent the start index in numbers
        :param end_index: Integer represent the end index in numbers
        :return: The maximum amount of money you can rob tonight without alerting the police
        """
        # Integer storing the maximum profit
        current_max_profit = 0

        # Integer storing the alter option for max profit
        optional_max_profit = 0

        # Loop to calculate the current maximum profit for the current value
        for index in range(start_index, end_index):
            # Updating the new max profit, and updating the optional max profit
            optional_max_profit, current_max_profit = current_max_profit, max(numbers[index] + optional_max_profit,
                                                                              current_max_profit)

        # Returning the maximum possible profit
        return current_max_profit

    # Returning the solution with error handling in case numbers length is 1
    return max(acyclic_rob(0, len(numbers) - 1), acyclic_rob(1, len(numbers))) if len(numbers) > 1 else numbers[0]
