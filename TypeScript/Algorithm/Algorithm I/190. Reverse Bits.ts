/**
 * Reverses the bits of a given integer.
 * @param {number} n - The integer whose bits are to be reversed.
 * @returns {number} The integer with reversed bits.
 */
function reverseBits(n: number): number {
  let reverseN: number = 0;

  for (let _: number = 0; _ < 31; _++) {
    reverseN = (reverseN + (n & 1)) * 2;
    n >>= 1;
  }

  reverseN = reverseN + (n & 1);
  return reverseN;
}
