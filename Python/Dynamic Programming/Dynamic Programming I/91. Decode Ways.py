def num_decodings(string: str) -> int:
    """
    Finding the amount of ways we can encode string, and return it
    Note : the encoding characters is from 1 to 26 include

    :param string: String asemble by digits
    :return: The amount of ways we can encode string

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # Edge case: the first character in string is 0 (0 doesn't have encoding value by itself)
    if string[0] == '0':
        return 0

    # Initialize nth_decodings_counter, each cell describe the amount of ways we can decode till him
    nth_decodings_counter = [0 for _ in range(len(string) + 1)]

    # Create the base case
    nth_decodings_counter[0] = nth_decodings_counter[1] = 1

    # Loop to traverse each cell in nth_decodings_counter and update accordingly to the current character in string
    for index in range(2, len(string) + 1):

        # Base case : if we can encode the current character, False only when char is '0'
        if string[index - 1] != '0':
            nth_decodings_counter[index] = nth_decodings_counter[index - 1]

        # if we can make encode the last 2 characters
        if 10 <= int(string[index - 2: index]) <= 26:
            nth_decodings_counter[index] += nth_decodings_counter[index - 2]

    # Returning the encoding counter at the last nth cell
    return nth_decodings_counter[-1]
