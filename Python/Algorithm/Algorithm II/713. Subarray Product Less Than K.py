def num_subarray_product_less_than_k(numbers: list[int], k: int) -> int:
    
    subarray_solution_counter = 0

    start_index = 0

    current_sum = 1

    for end_index, value in enumerate(numbers):

        current_sum *= value

        while current_sum >= k and start_index <= end_index:
            current_sum /= numbers[start_index]
            start_index += 1

        subarray_solution_counter += (end_index - start_index + 1)

    return subarray_solution_counter
