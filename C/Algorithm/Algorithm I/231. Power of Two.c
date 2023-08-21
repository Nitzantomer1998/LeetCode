/*
 * Checks if an integer is a power of two.
 *
 * The 'isPowerOfTwo' function determines whether a given integer 'n' is a power of two.
 * It does so by performing a bitwise AND operation between 'n' and 'n - 1'. If the result
 * of this operation is zero and 'n' is not equal to zero, then 'n' is a power of two,
 * since powers of two have only a single '1' bit in their binary representation. If 'n'
 * is not a power of two or is zero, the function returns 'false'.
 *
 * Parameters:
 * - n: An integer to be checked for being a power of two.
 *
 * Returns:
 * 'true' if 'n' is a power of two, 'false' otherwise.
 *
 * This function efficiently determines whether the input integer is a power of two by
 * exploiting the binary representation properties of powers of two.
 */
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}
