def hamming_weight(number: int) -> int:
    
    ones_counter = 0

    while number:
        ones_counter += number & 1

        number >>= 1

    return ones_counter
