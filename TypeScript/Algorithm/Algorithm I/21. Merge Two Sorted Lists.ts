/**
 * Checks if a given number is a power of two.
 * @param {number} n - The number to be checked.
 * @returns {boolean} Returns true if the number is a power of two, otherwise false.
 */
function isPowerOfTwo(n: number): boolean {
    return (n & (n - 1)) === 0 && n > 0;
};
