def permute_unique(numbers: list[int]) -> list[list[int]]:
    
    permute_solution = []

    numbers.sort()

    def add_permute(numbers: list[int], current_permute: list[int]) -> None:
        
        if not numbers:
            permute_solution.append(current_permute)
            return

        for index in range(len(numbers)):

            if index > 0 and numbers[index] == numbers[index - 1]:
                continue

            add_permute(numbers[:index] + numbers[index + 1:], current_permute + [numbers[index]])

    add_permute(numbers, [])

    return permute_solution
