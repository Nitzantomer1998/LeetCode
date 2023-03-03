def max_profit(prices: list[int]) -> int:
    
    max_profit = 0

    min_purchase_price = prices[0]

    for i in range(1, len(prices)):
        current_profit = prices[i] - min_purchase_price

        max_profit = max(max_profit, current_profit)

        min_purchase_price = min(min_purchase_price, prices[i])

    return max_profit
