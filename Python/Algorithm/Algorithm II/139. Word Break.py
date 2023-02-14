def word_break(string: str, word_dict: list[str]) -> bool:
    
    nth_word_fit = [False] * len(string)

    nth_word_fit.append(True)

    for index in range(len(string) - 1, -1, -1):

        for word in word_dict:

            if (index + len(word)) <= len(string) and string[index: index + len(word)] == word:
                nth_word_fit[index] = nth_word_fit[index + len(word)]

            if nth_word_fit[index]:
                break

    return nth_word_fit[0]
