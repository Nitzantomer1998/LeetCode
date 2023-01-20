def reverse_words(string: str) -> str:
    
    words = string.split()

    words = [word[::-1] for word in words]

    return ' '.join(words)
