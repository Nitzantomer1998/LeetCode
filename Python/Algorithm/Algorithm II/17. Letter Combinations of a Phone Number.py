def letter_combinations(digits: str) -> list[str]:
    """
    Building all the possible letter combinations that the number could represent, and return it

    :param digits: String represent message using the old phone system
    :return: All the possible letter combinations that the number could represent

    Time Complexity: o(n * 4^n)
    Space Complexity: o(n * 4^n)
    """
    # if the digits string is empty, then there is no message to create
    if not digits:
        return []

    # Dictionary to hold the Digit : Char converter
    digit_char_converter = {'2': 'abc',
                            '3': 'def',
                            '4': 'ghi',
                            '5': 'jkl',
                            '6': 'mno',
                            '7': 'pqrs',
                            '8': 'tuv',
                            '9': 'wxyz'}

    # List of string storing the solution
    letter_combinations_solution = ['']

    # Loop to traverse the digits list
    for digit in digits:

        # List storing the current solution
        current_solution = []

        # Double loop to expand the existing strings such that we could add the new digit chars
        for index, string in enumerate(letter_combinations_solution):

            # Adding the new updated current string
            for j in range(len(digit_char_converter[digit])):
                current_solution.append(string + digit_char_converter[digit][j])

        # Update the solution strings
        letter_combinations_solution = current_solution

    # Returning all the possible letter combinations that the number could represent
    return letter_combinations_solution
