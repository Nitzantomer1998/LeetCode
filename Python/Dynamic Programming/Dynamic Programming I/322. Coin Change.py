def coin_change(coins: list[int], amount: int) -> int:
    
    MCN = [amount + 1] * (amount + 1)
    MCN[0] = 0

    for index in range(1, amount + 1):

        for coin in coins:
            if index >= coin:
                MCN[index] = min(MCN[index], 1 + MCN[index - coin])

    return MCN[-1] if MCN[-1] != amount + 1 else -1
