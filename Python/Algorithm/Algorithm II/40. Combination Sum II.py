def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    
    combinations_solution = []

    candidates.sort()

    def add_combination(index: int, current_sum: int, current_combination: list[int]) -> None:
        
        if current_sum == target:
            combinations_solution.append(current_combination)
            return

        elif current_sum > target:
            return

        for i in range(index + 1, len(candidates)):

            if i > index + 1 and candidates[i] == candidates[i - 1]:
                continue

            add_combination(i, current_sum + candidates[i], current_combination + [candidates[i]])

    add_combination(-1, 0, [])

    return combinations_solution
