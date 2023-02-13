def longest_palindrome(string: str) -> str:
    
    longest_palindrome_indices = [0, 0]

    def expand_center(left: int, right: int) -> list[int]:
        
        while 0 <= left <= right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return [left + 1, right]

    for i in range(len(string)):
        odd_case = expand_center(i, i)

        even_case = expand_center(i, i + 1)

        longest_palindrome_indices = max(longest_palindrome_indices, odd_case, even_case, key=lambda s: s[1] - s[0] + 1)

    return string[longest_palindrome_indices[0]: longest_palindrome_indices[1]]
