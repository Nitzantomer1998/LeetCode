def max_sub_array(numbers: list[int]) -> int:
    
    for index in range(len(numbers) - 2, -1, -1):

        if numbers[index] + numbers[index + 1] > numbers[index]:
            numbers[index] += numbers[index + 1]

    return max(numbers)
