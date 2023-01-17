def search_insert(numbers: list[int], target: int) -> int:
    insert_solution = 0

    left, right = 0, len(numbers) - 1

    while left <= right:

        middle = (right + left) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] > target:

            insert_solution = middle

            right = middle - 1

        else:

            insert_solution = middle + 1

            left = middle + 1

    return insert_solution
