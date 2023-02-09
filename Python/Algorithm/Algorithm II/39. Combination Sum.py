def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    
    combinations_solution = []

    def add_combination(index: int, current_sum: int, current_combination: list[int]) -> None:
        
        if current_sum == target:
            combinations_solution.append(current_combination)
            return

        elif current_sum > target:
            return

        for i in range(index, len(candidates)):
            add_combination(i, current_sum + candidates[i], current_combination + [candidates[i]])

    add_combination(0, 0, [])

    return combinations_solution
