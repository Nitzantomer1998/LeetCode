def rotate(numbers: list[int], step_amount: int) -> None:
    step_amount -= int(step_amount / len(numbers)) * len(numbers)

    def reverse(start: int, end: int) -> None:
        while start < end:
            numbers[start], numbers[end] = numbers[end], numbers[start]

            start += 1
            end -= 1

    reverse(0, len(numbers) - step_amount - 1)

    reverse(len(numbers) - step_amount, len(numbers) - 1)

    reverse(0, len(numbers) - 1)
