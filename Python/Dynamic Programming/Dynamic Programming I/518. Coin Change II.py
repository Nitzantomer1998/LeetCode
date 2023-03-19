def change(amount: int, coins: list[int]) -> int:
    
    num_combinations = [0] * (amount + 1)
    num_combinations[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            num_combinations[i] += num_combinations[i - coin]

    return num_combinations[amount]
