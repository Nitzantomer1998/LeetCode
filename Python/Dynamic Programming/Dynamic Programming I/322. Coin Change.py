def coin_change(coins: list[int], amount: int) -> int:
    """
    Finding the fewest number of coins that you need to make up to the sent amount, and return it
    Note : If that amount of money cannot be made up by any combination return 01

    :param coins: List of integers
    :param amount: Integer represent the amount of money we want to exchange with coins
    :return: The fewest number of coins that you need to make up to the sent amount if possible, else -1

    Time Complexity: o(n * m)
    Space Complexity: o(n)
    """
    # Initialize MCN with default value of amount + 1 as its highest amount of coins, MCN -> Minimum Coins Needed
    # Note : Each cell [i] will store the minimum needed coins for the amount i
    MCN = [amount + 1] * (amount + 1)
    MCN[0] = 0

    # Double loop for updating MCN
    for index in range(1, amount + 1):

        # Loop for checking the minimum amount of coins needed for the amount i
        for coin in coins:
            if index >= coin:
                MCN[index] = min(MCN[index], 1 + MCN[index - coin])

    # Returning the fewest number of coins that you need to make up to the sent amount if possible, else -1
    return MCN[-1] if MCN[-1] != amount + 1 else -1
