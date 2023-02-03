def backspace_compare(s: str, t: str) -> bool:
    """
    Checking if the two string are equal, and return accordingly
    Note : The character '#' allows you to ignore a character on his left

    :param s: String filled with lowercase and '#'
    :param t: String filled with lowercase and '#'
    :return: True if the two string are equal, else False

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # I & J Pointers for the last index of s & t
    i = len(s) - 1
    j = len(t) - 1

    # counter_s & counter_t Counters for the '#' instances in s & t
    counter_s = 0
    counter_t = 0

    # Loop to traverse all the strings characters
    while i >= 0 or j >= 0:

        # Loop to update I index to point to the right s index that affect by the '#' symbol
        # Note : The loop will happen only if the '#' counter is positive or the current char is '#'
        while i >= 0 and (counter_s > 0 or s[i] == '#'):

            # if s current char is '#' than increase s '#' counter
            if s[i] == '#':
                counter_s += 1

            # if s current isn't '#' than decrease s '#' counter
            else:
                counter_s -= 1

            # Update i for the next iteration
            i -= 1

        # Loop to update J index to point to the right t index that affect by the '#' symbol
        # Note : The loop will happen only if the '#' counter is positive or the current char is '#'
        while j >= 0 and (counter_t > 0 or t[j] == '#'):

            # if t current char is '#' than increase t '#' counter
            if t[j] == '#':
                counter_t += 1

            # if t current isn't '#' than decrease t '#' counter
            else:
                counter_t -= 1

            # Update j for the next iteration
            j -= 1

        # After getting the right indices of each string, we store the current char, + special char in case of an error
        s_current_char = None if i < 0 else s[i]
        t_current_char = None if j < 0 else t[j]

        # if the current char of each string is different the strings aren't match, return False
        if s_current_char != t_current_char:
            return False

        # Update the pointers for the next iteration
        i -= 1
        j -= 1

    # if the while loop end, means we have the same string, return True
    return True
