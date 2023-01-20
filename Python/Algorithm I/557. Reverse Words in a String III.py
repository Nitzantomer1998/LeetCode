def reverse_words(string: str) -> str:
    """
    Reversing the order of characters in each word within a sentence, and return it

    :param string: String represent a sentence
    :return: The sentence which every word is reversed

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # Creating list, which every index of her hold a full word from string
    words = string.split()

    # Reversing every word in words
    words = [word[::-1] for word in words]

    # Returning the reversed string, by adding spacebar between every two words
    return ' '.join(words)
