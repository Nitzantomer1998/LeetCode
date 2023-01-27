def letter_case_permutation(string: str) -> list[str]:
   
    permutation_solution = []

    def add_permutation(index: int, current_list: list[str]) -> None:
        
        if index == len(string):
            permutation_solution.append(''.join(current_list))
            return

        if '0' <= string[index] <= '9':
            add_permutation(index + 1, current_list + [string[index]])

        else:
            add_permutation(index + 1, current_list + [string[index]])
            add_permutation(index + 1, current_list + [string[index].swapcase()])

    add_permutation(0, [])

    return permutation_solution
