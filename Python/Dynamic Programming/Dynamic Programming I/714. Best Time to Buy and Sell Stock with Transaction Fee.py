def max_profit(stock_prices: list[int], fee: int) -> int:
    """
    Find the maximum profit that can be achieved by buying and selling stocks on different days.
    You may make multiple transactions, as long as you sell stocks before you buy again.
    After selling a stock, there is a cooldown period of 1 day.

    :param stock_prices: A list of integers representing the stock prices on different days.
    :param fee: An integer representing the transaction fee for each sale.
    :return: An integer representing the maximum profit that can be made.

    Time Complexity: o(n)
    Space Complexity: o(n)
    """

    # Dictionary to store calculated profits
    profit_dict = {}

    def calculate_profit(day: int, has_stock: bool) -> int:
        if day >= len(stock_prices):
            return 0

        if (day, has_stock) in profit_dict:
            return profit_dict[(day, has_stock)]

        # Calculate profit if no transaction is made on this day
        cooldown_profit = calculate_profit(day + 1, has_stock)

        if has_stock:
            # Calculate profit if stock is sold on this day
            sell_profit = calculate_profit(day + 1, False) + stock_prices[day] - fee
            profit_dict[(day, has_stock)] = max(sell_profit, cooldown_profit)
        else:
            # Calculate profit if stock is bought on this day
            buy_profit = calculate_profit(day + 1, True) - stock_prices[day]
            profit_dict[(day, has_stock)] = max(buy_profit, cooldown_profit)

        return profit_dict[(day, has_stock)]

    return calculate_profit(0, False)
