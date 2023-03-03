def max_profit(prices: list[int]) -> int:
    
    current_hold, current_not_hold = -float('inf'), 0

    for stock_price in prices:
        previous_hold, previous_not_hold = current_hold, current_not_hold

        current_hold = max(previous_hold, previous_not_hold - stock_price)

        current_not_hold = max(previous_not_hold, previous_hold + stock_price)

    return current_not_hold
