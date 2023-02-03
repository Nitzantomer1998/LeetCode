def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Finding two indices in numbers which their summation is equal to target, and return their indices
    Note: numbers is sorted by non-decreasing order

    :param numbers: List of integers
    :param target: Integer represent target to achieve by summation of two integers in numbers
    :return: Two indices in numbers which their summation is equal to target

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Left & Right pointers for the start and the end of numbers
    left, right = 0, len(numbers) - 1

    # Loop to traverse the pointers left and right, in order to achieve the desire target
    while left < right:

        current_sum = numbers[left] + numbers[right]

        # if the current sum is larger than target, than we need to lower the sum, therefor right moving to the left
        if current_sum > target:
            right -= 1

        # if the current sum is lower than target, than we need to enlarge the sum, therefor left moving to the right
        elif current_sum < target:
            left += 1

        # We got the desirable target, return the solution
        else:

            # Returning the solution indices, Note: LeetCode first index start from 1 not 0
            return [left + 1, right + 1]
