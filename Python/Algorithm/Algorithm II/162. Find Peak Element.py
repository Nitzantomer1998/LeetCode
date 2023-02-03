def find_peak_element(numbers: list[int]) -> int:
    """
    Find an index element in numbers, that is bigger than his right and left neighbors, and return it

    :param numbers: List of integers
    :return: The index which both of his neighbors is lower than him

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Binary Search Algorithm
    # Left & Right pointer to traverse the sorted list
    left, right = 0, len(numbers) - 1

    # Loop to traverse the list
    while left < right:

        # Integer storing the middle index
        middle = (left + right) // 2

        # if numbers[middle] is bigger than his neighbors, then we found the peak solution, return it
        if numbers[middle] > numbers[middle + 1] and numbers[middle] > numbers[middle - 1]:
            return middle

        # if numbers[middle] is smaller than the next value, update left to be middle + 1
        elif numbers[middle] < numbers[middle + 1]:
            left = middle + 1

        # if numbers[middle] is bigger than the next value, update right to be middle - 1
        else:
            right = middle - 1

    # return the index solution
    return left
