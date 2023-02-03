def hamming_weight(number: int) -> int:
    """
    counting the amount of 1 value bits in number, and return it

    :param number: Unsigned Integer represented in the bit presentation
    :return: The amount of 1 value bits in number

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Variable Storing the value 1 bits counter
    ones_counter = 0

    # Loop to traverse every bit in number
    while number:
        # Note : & operator performs bit by bit AND operation on the two values,
        # if both bits equals 1 then output 1, else 0.
        # Therefor number & 1 return 1 only if the LSB bit in number is 1, else 0
        # so our counter will be updated according to the bit
        ones_counter += number & 1

        # Updating the terms for the next iteration
        # Note : >> operator performs shift to right by number of bits stipulated by second operand, for now is 1
        number >>= 1

    # Returning the amount of 1 value bits in number
    return ones_counter
