def combine(number: int, k: int) -> list[list[int]]:
    
    MAX_VALUE = number + 1
    PERMUTATION_LENGTH = k

    permutation_solution = []

    def add_nth_permutation(current_digit: int, current_permutation: list[int]) -> None:
       
        if len(current_permutation) == PERMUTATION_LENGTH:
            permutation_solution.append(current_permutation)
            return

        for next_digit in range(current_digit + 1, MAX_VALUE):
            add_nth_permutation(next_digit, current_permutation + [next_digit])

    for digit in range(1, MAX_VALUE):
        add_nth_permutation(digit, [digit])

    return permutation_solution
