def length_of_longest_substring(string: str) -> str:
    """
    Finding the maximum length of a non-duplicate substring of the sent string, and return it

    :param string: String
    :return: The maximum length of non-duplicate substring

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable to store the longest length of a substring
    longest_substring_length = 0

    # Dictionary to store [Char : Index] pairs of the visited characters
    char_dictionary = {}

    # Start index of the substring
    start_index = 0

    # Loop to traverse every character in the string
    for index, char in enumerate(string):

        # if we found a duplicate char in the current substring, update the start index of the new substring
        if char in char_dictionary and start_index <= char_dictionary[char]:
            start_index = char_dictionary[char] + 1

        # if the current substring didn't end, update the maximum substring length
        else:
            longest_substring_length = max(longest_substring_length, index - start_index + 1)

        # Add the current pair [Char : Index] into the char dictionary
        char_dictionary[char] = index

    # Return the longest substring length
    return longest_substring_length
