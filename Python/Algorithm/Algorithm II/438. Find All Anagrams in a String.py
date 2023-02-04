def find_anagrams(string: str, pattern: str) -> list[int]:
    """
    Finding all the starting indices that pattern showed in string, no matter the order of the characters, and return it

    :param string: String
    :param pattern: String
    :return: The starting indices that pattern showed in string, no matter the order of the characters

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # List storing the starting indices which pattern is in string
    anagram_solution = []

    # Lists storing the characters counter for each one of them
    # Note : Cell 0 equal to char 'a', and cell 25 equal to 'z'
    pattern_chars_counter = [0] * 26
    window_chars_counter = [0] * 26

    # Initialize pattern chars counter
    for char in pattern:
        pattern_chars_counter[ord(char) - ord('a')] += 1

    # Pointer representing the start index of the current window
    start_index = 0

    # Loop to traverse each character in string
    for end_index, char in enumerate(string):

        # Integer storing the right cell index in the lists of the current char, for better readability code
        index = ord(char) - ord('a')

        # if adding the current char will enlarge the window, then update the window chars counter
        if window_chars_counter[index] < pattern_chars_counter[index]:
            window_chars_counter[index] += 1

        # if adding the current char will harm the window, then there's two cases
        else:

            # First case : The current char exist in pattern, but it's passing the instances amount of it in window
            if pattern_chars_counter[index] > 0:

                # Fixing portion of the window chars counter, and start index, till the window is valid again
                while string[start_index] != char:
                    window_chars_counter[ord(string[start_index]) - ord('a')] -= 1
                    start_index += 1

            # Second case : The current char doesn't exist in pattern
            else:

                # Reset the current window for the next iteration (window char counter, and start index)
                while start_index < end_index:
                    window_chars_counter[ord(string[start_index]) - ord('a')] -= 1
                    start_index += 1

            # Updating the start index for the next iteration
            start_index += 1

        # if the current window length match to the pattern length, we found a substring
        if end_index - start_index == len(pattern) - 1:
            # Adding the starting index of the current window to the solution
            anagram_solution.append(start_index)

            # Updating window char counter and start_index for the next iteration
            window_chars_counter[ord(string[start_index]) - ord('a')] -= 1
            start_index += 1

    # Returning all starting index of pattern that in string
    return anagram_solution
