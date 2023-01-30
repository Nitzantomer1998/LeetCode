def reverse_bits(number: int) -> int:
    """
    Reversing the bits of a given 32 bits unsigned integer, and return it

    :param number: 32 bits unsigned integer
    :return: The reversed bits of number

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable to store the reverse bits of number
    reversed_bits_solution = 0

    # Loop to traverse each bit
    for _ in range(32):
        # Update the reversed_bits_solution, by shift to left once and insert the new bit
        reversed_bits_solution = (reversed_bits_solution << 1) + (number & 1)

        # Update the number by shift to right once, which will give us the next bit
        number >>= 1

    # Return the reversed bit
    return reversed_bits_solution
