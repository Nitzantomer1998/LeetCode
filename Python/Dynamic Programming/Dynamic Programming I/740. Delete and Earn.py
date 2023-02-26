from collections import Counter


def delete_and_earn(numbers: list[int]) -> int:
    
    counter = Counter(numbers)

    numbers = sorted(list(set(numbers)))

    previous_earn = max_earn = 0

    for index, value in enumerate(numbers):

        current_earn = numbers[index] * counter[value]

        if index > 0 and numbers[index] == numbers[index - 1] + 1:

            previous_earn, max_earn = max_earn, max(current_earn + previous_earn, max_earn)

        else:

            previous_earn, max_earn = max_earn, current_earn + max_earn

    return max_earn
