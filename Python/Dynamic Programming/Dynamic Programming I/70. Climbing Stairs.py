def climb_stairs(n: int) -> int:
    
    current_climb_options = 1

    previous_climb_options = 1

    for index in range(n - 1):
        current_climb_options, previous_climb_options = current_climb_options + previous_climb_options, current_climb_options

    return current_climb_options
