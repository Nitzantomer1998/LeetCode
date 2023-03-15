def longest_palindrome_subseq(string: str) -> int:
    
    n = len(string)

    longest_subseq_lengths = [[0] * n for _ in range(n)]

    for i in range(n):
        longest_subseq_lengths[i][i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if string[i] == string[j]:
               
                longest_subseq_lengths[i][j] = longest_subseq_lengths[i + 1][j - 1] + 2
            else:
               
                longest_subseq_lengths[i][j] = max(longest_subseq_lengths[i + 1][j], longest_subseq_lengths[i][j - 1])

    return longest_subseq_lengths[0][-1]
