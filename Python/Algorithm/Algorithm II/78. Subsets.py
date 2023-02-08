def subsets(numbers: list[int]) -> list[list[int]]:
   
    subsets_solution = []

    def add_subset(index: int, current_subset: list[int]) -> None:
       
        subsets_solution.append(current_subset)

        for next_index in range(index, len(numbers)):
            add_subset(next_index + 1, current_subset + [numbers[next_index]])

    add_subset(0, [])

    return subsets_solution
