def max_product(numbers: list[int]) -> int:
    
    current_max, current_min = 1, 1

    result = numbers[0]

    for value in numbers:
        values = (value, value * current_max, value * current_min)

        current_max, current_min = max(values), min(values)

        result = max(result, current_max)

    return result
