def rob(numbers: list[int]) -> int:
    """
    Finding the maximum amount of money you can rob tonight without alerting the police, and return it
    Note : if you visit an adjacent the cops will show up

    :param numbers: List of integers Representing amount of money in each house
    :return: The maximum amount of money you can rob tonight without alerting the police

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable to store the maximum profit
    current_max_profit = 0

    # Variable to hold the alter option for max profit
    optional_max_profit = 0

    # Loop to calculate the current maximum profit for the current value
    for value in numbers:
        # Updating the new max profit, and updating the optional max profit
        optional_max_profit, current_max_profit = current_max_profit, max(value + optional_max_profit,
                                                                          current_max_profit)

    # Returning the maximum possible profit
    return current_max_profit
