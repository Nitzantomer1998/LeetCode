def min_sub_array_len(target: int, numbers: list[int]) -> int:
    
    min_subarray_solution = len(numbers) + 1

    start_index = 0

    current_sum = 0

    for end_index, value in enumerate(numbers):

        current_sum += value

        while current_sum >= target and start_index <= end_index:
            min_subarray_solution = min(min_subarray_solution, end_index - start_index + 1)

            current_sum -= numbers[start_index]
            start_index += 1

    return min_subarray_solution if min_subarray_solution <= len(numbers) else 0
