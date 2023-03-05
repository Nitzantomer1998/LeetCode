def max_profit(prices: list[int]) -> int:
    
    max_profit_today = [0] * len(prices)
    max_profit_sell_today = [0] * len(prices)

    for i in range(1, len(prices)):
        
        for j in range(i):
            profit = prices[i] - prices[j] + (max_profit_today[j - 2] if j >= 2 else 0)
            max_profit_sell_today[i] = max(max_profit_sell_today[i], profit)

        max_profit_today[i] = max(max_profit_today[i - 1], max_profit_sell_today[i])
        
    return max_profit_today[-1]
