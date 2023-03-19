def change(amount: int, coins: list[int]) -> int:
    """
    Find the number of combinations of coins that add up to the given amount, and return it

    :param amount: The target amount of money.
    :param coins: The list of coin denominations.
    :return: The number of combinations of coins that add up to the target amount.

    Time Complexity: o(amount * len(coins))
    Space Complexity: o(amount)
    """
    # Initialize dp table with base case
    num_combinations = [0] * (amount + 1)
    num_combinations[0] = 1

    # Iterate over coins and fill in dp table
    for coin in coins:
        for i in range(coin, amount + 1):
            num_combinations[i] += num_combinations[i - coin]

    # Return the answer
    return num_combinations[amount]
