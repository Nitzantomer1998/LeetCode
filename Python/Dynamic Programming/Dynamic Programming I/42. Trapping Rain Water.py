def trap(height: list[int]) -> int:
    """
    Compute how much water an elevation map can trap after raining.

    :param height: A list of non-negative integers representing the height of each bar in the elevation map.
    :returns: The amount of water that can be trapped after raining.

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # If the height array is empty, we cannot trap any water, so return 0.
    if not height:
        return 0

    # Initialize two pointers - left and right - to the beginning and end of the height array, respectively.
    # Also initialize two variables - left_max and right_max - to keep track of the maximum heights seen so far on the left and right sides, respectively.
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    # Initialize a variable to keep track of the trapped water.
    trapped_water = 0

    # Iterate while the left pointer is less than the right pointer.
    while left < right:
        # If the height at the left pointer is less than or equal to the height at the right pointer,
        if height[left] <= height[right]:
            # Move the left pointer one step to the right.
            left += 1
            # Update the left_max variable to be the maximum of the current left_max and the height at the new left pointer.
            left_max = max(left_max, height[left])
            # Add the difference between left_max and the height at the new left pointer to the trapped_water variable.
            trapped_water += left_max - height[left]
        else:
            # If the height at the right pointer is greater than the height at the left pointer,
            # move the right pointer one step to the left.
            right -= 1
            # Update the right_max variable to be the maximum of the current right_max and the height at the new right pointer.
            right_max = max(right_max, height[right])
            # Add the difference between right_max and the height at the new right pointer to the trapped_water variable.
            trapped_water += right_max - height[right]

    # After the iteration is complete, return the trapped_water variable.
    return trapped_water
