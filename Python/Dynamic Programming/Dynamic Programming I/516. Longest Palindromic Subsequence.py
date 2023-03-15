def longest_palindrome_subseq(string: str) -> int:
    """
    Finds the length of the longest palindromic subsequence in the given string.

    :param string: A string.
    :return: The length of the longest palindromic subsequence in the string.

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n ^ 2)
    """

    # Get the length of the input string
    n = len(string)

    # Initialize a 2D array to store the lengths of the longest palindromic subsequences
    # in each substring
    longest_subseq_lengths = [[0] * n for _ in range(n)]

    # Base case: a single character is always a palindrome
    for i in range(n):
        longest_subseq_lengths[i][i] = 1

    # Fill in the longest_subseq_lengths array using dynamic programming
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if string[i] == string[j]:
                # If the characters at the start and end of the substring match,
                # the length of the longest palindromic subsequence is the length
                # of the longest palindromic subsequence of the substring without
                # the start and end characters plus two (to include the start and end characters)
                longest_subseq_lengths[i][j] = longest_subseq_lengths[i + 1][j - 1] + 2
            else:
                # If the characters at the start and end of the substring do not match,
                # the length of the longest palindromic subsequence is the maximum of
                # the lengths of the longest palindromic subsequences of the substrings
                # without the start and end characters
                longest_subseq_lengths[i][j] = max(longest_subseq_lengths[i + 1][j], longest_subseq_lengths[i][j - 1])

    # Return the length of the longest palindromic subsequence in the whole string
    return longest_subseq_lengths[0][-1]
