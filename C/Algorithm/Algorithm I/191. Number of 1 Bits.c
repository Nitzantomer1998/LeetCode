/*
 * Counts the number of '1' bits in the binary representation of a 32-bit unsigned integer.
 *
 * The 'hammingWeight' function calculates the Hamming weight, which represents the
 * number of '1' bits in the binary representation of a given 32-bit unsigned integer 'n'.
 * It iterates through each bit of the integer, checking if the least significant bit
 * (LSB) is '1'. If it is, the function increments the 'oneCounter' to keep track of the
 * number of '1' bits. The input integer is then right-shifted by one position in each
 * iteration to move to the next bit.
 *
 * Parameters:
 * - n: A 32-bit unsigned integer for which the Hamming weight needs to be calculated.
 *
 * Returns:
 * The count of '1' bits (Hamming weight) in the binary representation of the input integer.
 *
 * This function efficiently calculates the Hamming weight by examining each bit of the
 * input integer and incrementing the counter when a '1' bit is encountered. The final
 * result represents the number of '1' bits in the binary representation of 'n'.
 */
int hammingWeight(uint32_t n) {
    int oneBitCounter = 0;

    for (int index = 32; index > 0; index--) {
        if (n & 1)
            oneBitCounter++;

        n >>= 1;
    }

    return oneBitCounter;
}
