/*
 * Reverses the bits of a 32-bit unsigned integer.
 *
 * The 'reverseBits' function takes a 32-bit unsigned integer 'n' as input and reverses
 * its binary representation to obtain a new unsigned integer. It iterates through each
 * bit of the input integer from the least significant bit (LSB) to the most significant
 * bit (MSB). During each iteration, it appends the current bit to the result after
 * shifting the result one position to the left (multiplying by 2). After processing all
 * bits, the function returns the reversed integer.
 *
 * Parameters:
 * - n: A 32-bit unsigned integer to be reversed.
 *
 * Returns:
 * A new 32-bit unsigned integer with its bits reversed.
 *
 * This function efficiently reverses the bits of the input integer by considering each
 * bit's position and appending it to the result. The final result represents the binary
 * reversal of the input integer.
 */
uint32_t reverseBits(uint32_t n) {
    int reverseBitsValue = 0;
    
    for (int index = 31; index > 0; index--) {
        reverseBitsValue = (reverseBitsValue + (n & 1)) * 2;
        n >>= 1;
    }

    reverseBitsValue = (reverseBitsValue + (n & 1));
    return reverseBitsValue;
}
