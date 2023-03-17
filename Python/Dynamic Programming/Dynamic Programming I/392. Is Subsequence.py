def is_subsequence(s: str, t: str) -> bool:
    """
    Check whether s is a subsequence of t, and return it

    :param s: the subsequence we are searching for.
    :param t: the string we are searching in.
    :return: True if s is a subsequence of t, False otherwise.

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # initialize two pointers to the start of each string
    s_ptr = 0
    t_ptr = 0

    # iterate through the characters in both strings
    while s_ptr < len(s) and t_ptr < len(t):
        # if the characters match, move to the next character in s
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        # always move to the next character in t
        t_ptr += 1

    # if we've reached the end of s, all characters have been found in t
    return s_ptr == len(s)
