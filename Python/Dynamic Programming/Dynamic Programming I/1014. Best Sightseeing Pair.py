def max_score_sightseeing_pair(values: list[int]) -> int:
    """
    Find the maximum score of a pair of sightseeing spots, and return it
    Note: formula for a score is : values[i] + values[j] + i - j, Where i > j

    :param values: List of integers representing the value of sights on the spot
    :return: The maximum score of a pair of sightseeing spots

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Initialize maximum score
    max_score = 0

    # Initialize current maximum score
    current_max = 0

    for i in range(1, len(values)):
        # Calculate the current maximum score and update if needed
        current_max = max(current_max, values[i - 1] + i - 1)

        # Calculate the maximum score and update if needed
        max_score = max(max_score, current_max + values[i] - i)

    # Return the maximum score
    return max_score
