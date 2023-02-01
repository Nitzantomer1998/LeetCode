def find_peak_element(numbers: list[int]) -> int:
    
    left, right = 0, len(numbers) - 1

    while left < right:

        middle = (left + right) // 2

        if numbers[middle] > numbers[middle + 1] and numbers[middle] > numbers[middle - 1]:
            return middle

        elif numbers[middle] < numbers[middle + 1]:
            left = middle + 1

        else:
            right = middle - 1

    return left
