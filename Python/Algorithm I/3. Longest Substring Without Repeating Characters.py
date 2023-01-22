def length_of_longest_substring(string: str) -> str:
    
    longest_substring_length = 0

    char_dictionary = {}

    start_index = 0

    for index, char in enumerate(string):

        if char in char_dictionary and start_index <= char_dictionary[char]:
            start_index = char_dictionary[char] + 1

        else:
            longest_substring_length = max(longest_substring_length, index - start_index + 1)

        char_dictionary[char] = index

    return longest_substring_length
