def search(numbers: list[int], target: int) -> int:
    """
    Finding the index of target in numbers list, and return it
    Note : numbers is sorted list but its may have been shift rotated right

    :param numbers: Sorted integer list, that might have been shift rotated right
    :param target: Integer representing a value we are searching for in numbers
    :return: The index of target in numbers list if found, else -1

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Left & Right pointer to traverse the "sorted" list
    left, right = 0, len(numbers) - 1

    # Loop to traverse the list
    while left < right:

        # Integer storing the middle index
        middle = (left + right) // 2

        # if we found the target index than return it
        if numbers[middle] == target:
            return middle

        # if the [left, middle] indices of the list is in ascending order, means regular binary search
        elif numbers[left] <= numbers[middle]:

            # if target is in the section [left, middle], then update the right to be middle - 1
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1

            # if target isn't in the section [left, middle] than update left to be middle + 1
            else:
                left = middle + 1

        # if the [middle, right] indices of the list is in ascending order, means regular binary search
        else:

            # if target is in the section [middle, right], then update the left to be middle + 1
            if numbers[middle] < target <= numbers[right]:
                left = middle + 1

            # if target isn't in the section [middle, right] than update right to be middle - 1
            else:
                right = middle - 1

    # Returning the left index if match to target, else default error value
    return left if numbers[left] == target else -1
