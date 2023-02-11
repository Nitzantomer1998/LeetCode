def can_jump(numbers: list[int]) -> bool:
    
    target_index = len(numbers) - 1

    for index in range(len(numbers) - 1, -1, -1):

        if index + numbers[index] >= target_index:
            target_index = index

    return True if target_index == 0 else False
