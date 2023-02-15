def length_of_LIS(numbers: list[int]) -> int:
    """
    Finding the length of the longest strictly increasing subsequence in numbers, and return it

    :param numbers: List of integers
    :return: The length of the longest strictly increasing subsequence in numbers

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n)
    """
    # Initialize LIS with default value of 1, cause each cell in numbers is a sequence by itself therefore 1
    LIS = [1] * len(numbers)

    # Loop to traverse each number in numbers from end to start
    for i in range(len(numbers) - 1, -1, -1):

        # Loop to traverse numbers from i + 1 till the end, for checking after previous sequences
        for j in range(i + 1, len(numbers)):

            # if current value (i) is smaller than previous (j) update LIS[i] sequence length to be LIS[j] + 1 if bigger
            if numbers[i] < numbers[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    # Returning the maximum sequence length
    return max(LIS)
