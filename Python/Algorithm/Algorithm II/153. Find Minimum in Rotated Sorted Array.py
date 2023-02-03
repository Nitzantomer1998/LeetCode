def find_min(numbers: list[int]) -> int:
    """
    Finding the value of the minimum integer in numbers list, and return it
    Note : numbers is sorted list but its may have been shift rotated right

    :param numbers: Sorted integer list, that might have been shift rotated right
    :return: The value of the minimum integer in numbers list

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Binary Search Algorithm
    # Left & Right pointer to traverse the sorted list
    left, right = 0, len(numbers) - 1

    # Loop to traverse the list
    while left <= right:

        # Integer storing the middle index
        middle = (left + right) // 2

        # if numbers[left, middle] is an ascending order
        if numbers[left] <= numbers[middle]:

            # if numbers[left] is truly the minimum value return it
            if numbers[left] <= numbers[right]:
                return numbers[left]

            # if numbers[left] wasn't the minimum value, then update left to be middle + 1
            else:
                left = middle + 1

        # if numbers[left, middle] wasn't in ascending order means the minimum value is in numbers[left, middle]
        # Update right to be middle
        else:
            right = middle
