def search_range(numbers: list[int], target: int) -> list[int]:
    """
    Finding the start and end index of the value target in numbers, and return it indices
    Note : Numbers is sorted by non-decreasing order, and if index of target doesn't exist return [-1, -1]

    :param numbers: List of integers that sorted in non-decreasing order
    :param target: Integer representing a value we are searching for his index in numbers
    :return: The start and end index of the value target in numbers if found, else -1

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """

    # Assisting function to make the index search
    def binary_search(first_of_index: bool) -> int:
        """
        Finding the first / last index of target in numbers, and return it

        :param first_of_index: Boolean representing if we are searching for the first or last index of target
        :return: The first / end index of target in numbers if found, else -1
        """
        # Integer storing the index of target, initialize to -1 (error / default)
        target_index = -1

        # Left & Right pointer to traverse the sorted list
        left, right = 0, len(numbers) - 1

        # Loop to traverse the list
        while left <= right:

            # Integer storing the middle index
            middle = (left + right) // 2

            # if the middle index of number is equal to target, then update target_index
            if numbers[middle] == target:
                target_index = middle

                # if we search for the first index of target, then keep looking on the left side
                if first_of_index:
                    right = middle - 1

                # if we search for the last index of target, then keep looking on the right side
                else:
                    left = middle + 1

            # if the middle index of number is greater than target, then update right to be middle - 1
            elif numbers[middle] > target:
                right = middle - 1

            # if the middle index of number is lower than target, then update left to be middle + 1
            else:
                left = middle + 1

        # Returning the first / last index of target
        return target_index

    # Returning the start & end indices solution using callback for each index
    return [binary_search(True), binary_search(False)]
