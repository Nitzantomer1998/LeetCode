def max_profit(prices: list[int]) -> int:
    """
    Finds the maximum profit that can be achieved by buying and selling stocks on different days.
    Note: You may make couple transactions, as long you sell stocks before you buy

    :param prices: A list of integers representing the value of the stock on each day.
    :return: The maximum profit that can be achieved.

    :param prices: A list of integers representing the stock prices on different days.
    :return: An integer representing the maximum profit that can be made.

    Time Complexity: o(n)
    Space Complexity: o(1)
    """

    # Set the initial values for the hold and not hold states
    # It is impossible to sell stock on the first day, so we set current_hold to negative infinity
    current_hold, current_not_hold = -float('inf'), 0

    # Iterate over the stock prices
    for stock_price in prices:
        # Save the previous hold and not hold states
        previous_hold, previous_not_hold = current_hold, current_not_hold

        # Calculate the current hold state
        # Either keep hold, or buy in stock today at the stock price
        current_hold = max(previous_hold, previous_not_hold - stock_price)

        # Calculate the current not hold state
        # Either keep not-hold, or sell out stock today at the stock price
        current_not_hold = max(previous_not_hold, previous_hold + stock_price)

    # The maximum profit must be in the not-hold state
    return current_not_hold
