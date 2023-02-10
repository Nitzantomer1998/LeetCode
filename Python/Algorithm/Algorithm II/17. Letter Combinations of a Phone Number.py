def letter_combinations(digits: str) -> list[str]:

    if not digits:
        return []

    digit_char_converter = {'2': 'abc',
                            '3': 'def',
                            '4': 'ghi',
                            '5': 'jkl',
                            '6': 'mno',
                            '7': 'pqrs',
                            '8': 'tuv',
                            '9': 'wxyz'}

    letter_combinations_solution = ['']

    for digit in digits:

        current_solution = []

        for index, string in enumerate(letter_combinations_solution):

            for j in range(len(digit_char_converter[digit])):
                current_solution.append(string + digit_char_converter[digit][j])

        letter_combinations_solution = current_solution

    return letter_combinations_solution
