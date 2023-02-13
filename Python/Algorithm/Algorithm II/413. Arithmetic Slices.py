def number_of_arithmetic_slices(numbers: list[int]) -> int:
    
    nth_arithmetic_counter = [0] * len(numbers)

    for index in range(2, len(numbers)):

        if numbers[index] - numbers[index - 1] == numbers[index - 1] - numbers[index - 2]:
            nth_arithmetic_counter[index] = 1 + nth_arithmetic_counter[index - 1]

    return sum(nth_arithmetic_counter)
