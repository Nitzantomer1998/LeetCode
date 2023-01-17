def search(numbers: list[int], target: int) -> int:
     left, right = 0, len(numbers) - 1

    while left <= right:

        middle = (right + left) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] > target:
            right = middle - 1

        else:
            left = middle + 1

    return -1
