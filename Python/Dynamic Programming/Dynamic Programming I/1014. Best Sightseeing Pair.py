def max_score_sightseeing_pair(values: list[int]) -> int:
    
    max_score = 0

    current_max = 0

    for i in range(1, len(values)):
        current_max = max(current_max, values[i - 1] + i - 1)

        max_score = max(max_score, current_max + values[i] - i)

    return max_score
