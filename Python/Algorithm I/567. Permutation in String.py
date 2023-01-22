def check_inclusion(string1: str, string2: str) -> bool:
    """
    Checking if string2 contain a substring permutation of string1, return boolean accordingly

    :param string1: String containing lowercase english characters
    :param string2: String containing lowercase english characters
    :return: True if string2 contain a substring permutation of string1, else False

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Creating 2 lists for character counter of each string, 26 cells cause there are 26 english lowercase letters
    # Note: We use ascii values manipulation such that Cell 0 is 'a' and Cell 25 is 'z'
    string1_char_counter = [0] * 26
    string2_char_counter = [0] * 26

    # Initialize string1 char counter
    for char in string1:
        # "ord(char) - ord('a')" given us the numerical index of the current letter from 0 to 25 meaning 'a' to 'z'
        string1_char_counter[ord(char) - ord('a')] += 1

    # Loop to traverse string2 and update the list accordingly, and checking if we found a substring
    for index in range(len(string2)):

        # if the current window is bigger than string1 then we delete the last index of the current window
        # Note: current window is always in size of string1 length
        if index >= len(string1):
            string2_char_counter[ord(string2[index - len(string1)]) - ord('a')] -= 1

        # Update the char counter for string2
        string2_char_counter[ord(string2[index]) - ord('a')] += 1

        # if the list are identical than we found a substring, therefor return True
        if string1_char_counter == string2_char_counter:
            return True

    # if we reach here then string2 doesn't have a permutation of string1, therefor return False
    return False
