def wiggle_max_length(nums: list[int]) -> int:
    """
    Find the maximum value between the last element in the up array and the last element in the down array, and return it

    :param nums: List of integers
    :return: The maximum value between the last element in the up array and the last element in the down array

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # Holding the size of the list
    n = len(nums)

    # Base case, if the list is shorter than 2, so the Wiggle size is n
    if n < 2:
        return n

    # Initialize up and down arrays to 1
    up = [1] * n
    down = [1] * n

    # Loop through the array starting from the second element
    for i in range(1, n):

        # Check if the current element is greater than or less than the previous element
        if nums[i] > nums[i - 1]:
            # If it's greater, update the up array
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]

        elif nums[i] < nums[i - 1]:
            # If it's less, update the down array
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]

        else:
            # If it's equal, copy the values from the previous element
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    # Return the maximum value between the last element in the up array and the last element in the down array
    return max(up[-1], down[-1])
