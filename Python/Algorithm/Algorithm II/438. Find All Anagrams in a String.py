def find_anagrams(string: str, pattern: str) -> list[int]:
    
    anagram_solution = []

    pattern_chars_counter = [0] * 26
    window_chars_counter = [0] * 26

    for char in pattern:
        pattern_chars_counter[ord(char) - ord('a')] += 1

    start_index = 0

    for end_index, char in enumerate(string):

        index = ord(char) - ord('a')

        if window_chars_counter[index] < pattern_chars_counter[index]:
            window_chars_counter[index] += 1

        else:

            if pattern_chars_counter[index] > 0:

                while string[start_index] != char:
                    window_chars_counter[ord(string[start_index]) - ord('a')] -= 1
                    start_index += 1

            else:

                while start_index < end_index:
                    window_chars_counter[ord(string[start_index]) - ord('a')] -= 1
                    start_index += 1

            start_index += 1

        if end_index - start_index == len(pattern) - 1:
            anagram_solution.append(start_index)

            window_chars_counter[ord(string[start_index]) - ord('a')] -= 1
            start_index += 1

    return anagram_solution
