def rob(numbers: list[int]) -> int:
   
    def acyclic_rob(start_index: int, end_index: int) -> int:
        
        current_max_profit = 0

        optional_max_profit = 0

        for index in range(start_index, end_index):
            optional_max_profit, current_max_profit = current_max_profit, max(numbers[index] + optional_max_profit,
                                                                              current_max_profit)

        return current_max_profit

    return max(acyclic_rob(0, len(numbers) - 1), acyclic_rob(1, len(numbers))) if len(numbers) > 1 else numbers[0]
