def word_break(string: str, word_dict: list[str]) -> bool:
    """
    Finding if string can be segmented by a sequence from word_dict, and return accordingly

    :param string: String
    :param word_dict: List of words which we use to built string
    :return: True if string can be segmented by a sequence from word_dict, else False

    Time Complexity: o(n * m)
    Space Complexity: o(n)
    """
    # List storing in each cell True or False accordingly to a match between string and word_dict start in nth index
    nth_word_fit = [False] * len(string)

    # Append another cell to the end of the list, which will symbol success (if we reach there we found a full match)
    nth_word_fit.append(True)

    # Loop to traverse each character in string from end to start
    for index in range(len(string) - 1, -1, -1):

        # Loop to traverse each word in word_dict, and check for a match with the string
        for word in word_dict:

            # if adding the word keep us in boundaries, and the word is match to the specific indices in string, add it
            if (index + len(word)) <= len(string) and string[index: index + len(word)] == word:
                # Updating the cell according to his earlier match True / False (The loop traverse from end to start)
                nth_word_fit[index] = nth_word_fit[index + len(word)]

            # if the cell is already equal to True, means there's already a match word so stop looking for another one
            if nth_word_fit[index]:
                break

    # Returning the solution using nth_word_fit[0] which store True if there's a solution else False
    return nth_word_fit[0]
