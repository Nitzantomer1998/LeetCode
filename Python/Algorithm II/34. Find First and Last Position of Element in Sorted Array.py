def search_range(numbers: list[int], target: int) -> list[int]:

    def binary_search(first_of_index: bool) -> int:

        target_index = -1

        left, right = 0, len(numbers) - 1

        while left <= right:

            middle = (left + right) // 2

            if numbers[middle] == target:
                target_index = middle

                if first_of_index:
                    right = middle - 1

                else:
                    left = middle + 1

            elif numbers[middle] > target:
                right = middle - 1

            else:
                left = middle + 1

        return target_index

    return [binary_search(True), binary_search(False)]
