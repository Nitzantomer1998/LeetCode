def max_profit(stock_prices: list[int], fee: int) -> int:
    
    profit_dict = {}

    def calculate_profit(day: int, has_stock: bool) -> int:
        if day >= len(stock_prices):
            return 0

        if (day, has_stock) in profit_dict:
            return profit_dict[(day, has_stock)]

        cooldown_profit = calculate_profit(day + 1, has_stock)

        if has_stock:
            sell_profit = calculate_profit(day + 1, False) + stock_prices[day] - fee
            profit_dict[(day, has_stock)] = max(sell_profit, cooldown_profit)
        else:
            buy_profit = calculate_profit(day + 1, True) - stock_prices[day]
            profit_dict[(day, has_stock)] = max(buy_profit, cooldown_profit)

        return profit_dict[(day, has_stock)]

    return calculate_profit(0, False)
