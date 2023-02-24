def climb_stairs(n: int) -> int:
    """
    Finding the maximum ways you can climb n stairs, with the possibility of 1 or 2 steps each time, and return it

    :param n: Integer represent the amount of stairs
    :return: The maximum ways you can climb n stairs, with the possibility of 1 or 2 steps each time

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable to hold the amount of possible ways we can climb the stairs
    current_climb_options = 1

    # Variable to hold the possible next step in the stairs
    previous_climb_options = 1

    # Loop which run n - 1 steps, each iteration we calculate the amount of ways we can climb the index stair
    for index in range(n - 1):
        # Updating the new climbing stairs amount, and updating the previous climbing stairs amount
        current_climb_options, previous_climb_options = current_climb_options + previous_climb_options, current_climb_options

    # Returning the amount of possible ways to climb n stairs
    return current_climb_options
