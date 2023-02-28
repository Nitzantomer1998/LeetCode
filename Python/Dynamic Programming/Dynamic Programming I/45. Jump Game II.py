def jump(numbers: list[int]) -> int:
    
    min_jumps_made = 0

    left = right = 0

    while right < len(numbers) - 1:
        farthest = 0

        for index in range(left, right + 1):
            farthest = max(farthest, index + numbers[index])

        left = right + 1
        right = farthest
        min_jumps_made += 1

    return min_jumps_made
