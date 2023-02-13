def longest_palindrome(string: str) -> str:
    """
    Finding the longest palindrome that exist in the sent string, and return it

    :param string: String
    :return: The longest palindrome that exist in the sent string

    Time Complexity: o(n^2)
    Space Complexity: o(n)
    """
    # List of 2 integers representing the indices of the longest palindrome
    longest_palindrome_indices = [0, 0]

    # Function to check a palindrome by getting his middle indices and expanding outwards
    def expand_center(left: int, right: int) -> list[int]:
        """
        Finding the longest palindrome indices with the center of [left, right], and return it

        :param left: Left pointer, the start index for going outwards left
        :param right: Right pointer, the start index for going outwards right
        :return: The longest palindrome indices that start in index left, right
        """
        # Loop to expand string[left, right] outwards as long as it stay a palindrome
        while 0 <= left <= right < len(string) and string[left] == string[right]:
            # Updating the indices pointers to move outwards once for each side (enlarge the palindrome)
            left -= 1
            right += 1

        # Returning the longest palindrome that found for the sent indices
        return [left + 1, right]

    # Loop to traverse every character in our string
    for i in range(len(string)):
        # String length is Odd
        odd_case = expand_center(i, i)

        # String length is Even
        even_case = expand_center(i, i + 1)

        # Store in the solution the list indices with the maximum length
        longest_palindrome_indices = max(longest_palindrome_indices, odd_case, even_case, key=lambda s: s[1] - s[0] + 1)

    # Returning the biggest palindrome found
    return string[longest_palindrome_indices[0]: longest_palindrome_indices[1]]
