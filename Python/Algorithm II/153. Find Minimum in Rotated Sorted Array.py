def find_min(numbers: list[int]) -> int:
    
    left, right = 0, len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[left] <= numbers[middle]:

            if numbers[left] <= numbers[right]:
                return numbers[left]

            else:
                left = middle + 1

        else:
            right = middle
