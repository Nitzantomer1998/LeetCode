def generate_parenthesis(n: int) -> list[str]:
   
    parenthesis_solution = []

    def add_permutation(open_parenthesis: int, close_parenthesis: int, current_permutation: list[str]) -> None:
        
        if open_parenthesis == close_parenthesis == n:
            parenthesis_solution.append(''.join(current_permutation))
            return

        if open_parenthesis < n:
            add_permutation(open_parenthesis + 1, close_parenthesis, current_permutation + ['('])

        if close_parenthesis < open_parenthesis:
            add_permutation(open_parenthesis, close_parenthesis + 1, current_permutation + [')'])

    add_permutation(0, 0, [])

    return parenthesis_solution
