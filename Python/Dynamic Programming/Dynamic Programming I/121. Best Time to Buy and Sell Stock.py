def max_profit(prices: list[int]) -> int:
    """
    Finds the maximum profit that can be achieved by buying and selling stocks on different days.

    :param prices: A list of integers representing the value of the stock on each day.
    :return: The maximum profit that can be achieved.

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Initialize the maximum profit to zero
    max_profit = 0

    # Initialize the minimum purchase price to the first value in the prices list
    min_purchase_price = prices[0]

    # Iterate over the prices list
    for i in range(1, len(prices)):
        # Calculate the current profit
        current_profit = prices[i] - min_purchase_price

        # Update the maximum profit if the current profit is greater
        max_profit = max(max_profit, current_profit)

        # Update the minimum purchase price if the current price is lower
        min_purchase_price = min(min_purchase_price, prices[i])

    # Return the maximum profit that can be achieved
    return max_profit
