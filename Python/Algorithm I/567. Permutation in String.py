def check_inclusion(string1: str, string2: str) -> bool:
    
    string1_char_counter = [0] * 26
    string2_char_counter = [0] * 26

    for char in string1:
        string1_char_counter[ord(char) - ord('a')] += 1

    for index in range(len(string2)):

        if index >= len(string1):
            string2_char_counter[ord(string2[index - len(string1)]) - ord('a')] -= 1

        string2_char_counter[ord(string2[index]) - ord('a')] += 1

        if string1_char_counter == string2_char_counter:
            return True

    return False
