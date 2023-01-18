def sorted_squares(numbers: list[int]) -> list[int]:
    sorted_squares_solution = []

    left, right = 0, len(numbers) - 1

    while left <= right:

        if abs(numbers[left]) > abs(numbers[right]):

            sorted_squares_solution.append(numbers[left] ** 2)

            left += 1

        else:

            sorted_squares_solution.append(numbers[right] ** 2)

            right -= 1

    return sorted_squares_solution[::-1]
