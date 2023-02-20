def range_bitwise_and(left: int, right: int) -> int:
    
    shift_right_counter = 0

    while left != right:
        left >>= 1
        right >>= 1

        shift_right_counter += 1

    return left << shift_right_counter
