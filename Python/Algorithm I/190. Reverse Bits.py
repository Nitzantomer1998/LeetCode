def reverse_bits(number: int) -> int:
    
    reversed_bits_solution = 0

    for _ in range(32):
        reversed_bits_solution = (reversed_bits_solution << 1) + (number & 1)

        number >>= 1

    return reversed_bits_solution
