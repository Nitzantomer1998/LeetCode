def is_power_of_two(number: int) -> bool:
    
    return number > 0 and number & (number - 1) == 0
