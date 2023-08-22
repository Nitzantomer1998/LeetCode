/**
 * Calculates the Hamming weight (number of set bits) in a given integer.
 * @param {number} n - The integer for which to calculate the Hamming weight.
 * @returns {number} The count of set bits in the integer.
 */
function hammingWeight(n: number): number {
    let oneBitCounter: number = 0;

    for (let _: number = 0; _ < 32; _++) {
        oneBitCounter += n & 1;
        n >>= 1;
    }

    return oneBitCounter;
};
