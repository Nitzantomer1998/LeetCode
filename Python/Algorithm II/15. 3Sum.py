def three_sum(numbers: list[int]) -> list[list[int]]:
    
    numbers.sort()

    three_sum_solution = []

    for i in range(len(numbers) - 2):

        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        left, right = i + 1, len(numbers) - 1

        while left < right:

            current_sum = numbers[i] + numbers[left] + numbers[right]

            if current_sum > 0:
                right -= 1

            elif current_sum < 0:
                left += 1

            else:
                three_sum_solution.append([numbers[i], numbers[left], numbers[right]])

                left += 1

                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1

    return three_sum_solution
