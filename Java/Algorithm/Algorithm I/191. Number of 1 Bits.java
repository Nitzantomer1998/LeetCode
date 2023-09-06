public class Solution {

  /**
   * Counts the number of '1' bits in a 32-bit integer.
   *
   * @param n The 32-bit integer to count the '1' bits.
   * @return The number of '1' bits in the integer.
   */
  public int hammingWeight(int n) {
    int oneBitCounter = 0;

    for (int iteration = 0; iteration < 32; iteration++) {
      int LSB_Value = n & 1;
      oneBitCounter += LSB_Value;

      n >>= 1;
    }

    return oneBitCounter;
  }
}
