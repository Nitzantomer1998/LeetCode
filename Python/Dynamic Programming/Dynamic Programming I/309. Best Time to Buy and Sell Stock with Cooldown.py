def max_profit(prices: list[int]) -> int:
    """
    Find the maximum profit that can be achieved by buying and selling stocks on different days.
    You may make multiple transactions, as long as you sell stocks before you buy again.
    After selling a stock, there must be at least one day of cooldown before you can buy again.

    :param prices: A list of integers representing the stock prices on different days.
    :return: An integer representing the maximum profit that can be made.

    Time Complexity: o(n)
    Space Complexity: o(n)
    """

    # Initialize variables to keep track of the maximum profit
    # up to the current day, and the maximum profit that can be
    # achieved by selling on the current day.
    max_profit_today = [0] * len(prices)
    max_profit_sell_today = [0] * len(prices)

    for i in range(1, len(prices)):
        # Calculate the maximum profit that can be made by selling
        # on the current day, and update the max_profit_sell_today
        # list accordingly.
        for j in range(i):
            profit = prices[i] - prices[j] + (max_profit_today[j - 2] if j >= 2 else 0)
            max_profit_sell_today[i] = max(max_profit_sell_today[i], profit)

        # Update the max_profit_today list with the maximum profit
        # that can be achieved up to the current day, taking into
        # account the maximum profit that can be achieved by selling
        # on the current day.
        max_profit_today[i] = max(max_profit_today[i - 1], max_profit_sell_today[i])

    # Return the maximum profit that can be achieved by selling on
    # any day.
    return max_profit_today[-1]
