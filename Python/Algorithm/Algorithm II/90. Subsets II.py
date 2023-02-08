def subsets_with_dup(numbers: list[int]) -> list[list[int]]:
   
    subsets_solution = [[]]

    numbers.sort()

    previous_subsets_size = 0

    for i in range(len(numbers)):

        start_index = previous_subsets_size if i > 0 and numbers[i] == numbers[i - 1] else 0

        previous_subsets_size = len(subsets_solution)

        for j in range(start_index, previous_subsets_size):
            subsets_solution.append(subsets_solution[j] + [numbers[i]])

    return subsets_solution
