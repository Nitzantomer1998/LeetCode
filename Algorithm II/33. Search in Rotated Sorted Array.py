def search(numbers: list[int], target: int) -> int:
    
    left, right = 0, len(numbers) - 1

    while left < right:

        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[left] <= numbers[middle]:

            if numbers[left] <= target < numbers[middle]:
                right = middle - 1

            else:
                left = middle + 1

        else:

            if numbers[middle] < target <= numbers[right]:
                left = middle + 1

            else:
                right = middle - 1

    return left if numbers[left] == target else -1
