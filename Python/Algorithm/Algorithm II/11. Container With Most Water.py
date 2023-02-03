def max_area(heights: list[int]) -> int:
    """
    Finding the container with the maximum area, and return it
    Note : A container is made by two different heights from heights

    :param heights: List of integers
    :return: The container with the maximum area

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Integer storing the highest possible area value
    max_area_value = 0

    # Left & Right pointer to the start & end indices in heights
    left, right = 0, len(heights) - 1

    # Loop for finding the maximum area value, starting from the edges and slowly shrink itself
    while left < right:

        # Calculating the current area value, and then updating the max_area value if needed
        current_area = (right - left) * min(heights[left], heights[right])
        max_area_value = max(max_area_value, current_area)

        # if heights[left] smaller than height[right], than update left pointer to move one step forward
        if heights[left] < heights[right]:
            left += 1

        # if heights[right] smaller or equal to height[left], than update right pointer to move one step backward
        else:
            right -= 1

    # Returning the area of the maximum container
    return max_area_value
