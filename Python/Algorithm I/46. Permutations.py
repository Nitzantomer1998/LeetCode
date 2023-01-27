def permute(numbers: list[int]) -> list[list[int]]:
   
    permute_solution = []

    def add_permute(current_permute: list[int], digits_left: list[int]) -> None:
       
        if len(digits_left) == 0:
            permute_solution.append(current_permute)
            return

        for next_digit in digits_left:
            add_permute(current_permute + [next_digit], [digit for digit in digits_left if digit != next_digit])

    for digit in numbers:
        add_permute([digit], [value for value in numbers if value != digit])

    return permute_solution
