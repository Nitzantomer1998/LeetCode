def max_area(heights: list[int]) -> int:
    
    max_area_value = 0

    left, right = 0, len(heights) - 1

    while left < right:

        current_area = (right - left) * min(heights[left], heights[right])
        max_area_value = max(max_area_value, current_area)

        if heights[left] < heights[right]:
            left += 1

        else:
            right -= 1

    return max_area_value
