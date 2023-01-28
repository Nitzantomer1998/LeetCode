def rob(numbers: list[int]) -> int:
    
    current_max_profit = 0

    optional_max_profit = 0

    for value in numbers:
        optional_max_profit, current_max_profit = current_max_profit, max(value + optional_max_profit,
                                                                          current_max_profit)

    return current_max_profit
