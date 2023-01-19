def move_zeroes(numbers: list[int]) -> None:
    left, next_left = 0, 1

    while next_left < len(numbers):

        if numbers[left] == 0 and numbers[next_left] != 0:
            numbers[left], numbers[next_left] = numbers[next_left], numbers[left]

            left += 1
            next_left += 1

        elif numbers[left] == 0 and numbers[next_left] == 0:
            next_left += 1

        else:
            left += 1
            next_left += 1

    return
