def find_number_of_LIS(numbers: list[int]) -> int:
    """
    Finding the most frequent length of a strictly increasing subsequence in numbers, and return it

    :param numbers: List of integers
    :return: The most frequent length of a strictly increasing subsequence in numbers

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n)
    """
    # Initialize LIS with default value of 1, cause each cell in numbers is a sequence by itself therefore 1
    LIS = [1] * len(numbers)

    # Initialize SLC -> Sequence Length Counter
    SLC = [1] * len(numbers)

    # Loop to traverse each number in numbers, where increasing subsequence ending in numbers[i]
    for i in range(len(numbers)):

        # Loop to traverse every number before i, for checking after previous sequences
        for j in range(i):

            # if current value (i) is bigger than (j) update LIS[i] sequence length to be LIS[j] + 1 if bigger
            if numbers[i] > numbers[j]:

                # if the sequence that end in j is bigger than i, update i LIS and SLC
                if LIS[i] < LIS[j] + 1:
                    LIS[i] = LIS[j] + 1
                    SLC[i] = SLC[j]

                # if both of the sequence in the same length, update SLC[i]
                elif LIS[i] == LIS[j] + 1:
                    SLC[i] += SLC[j]

    # Integer storing the length of the longest increasing subsequence
    max_length = max(LIS)

    # Return the most frequent length of a strictly increasing subsequence
    return sum(count for length, count in zip(LIS, SLC) if length == max_length)
