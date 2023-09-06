public class Solution {

  /**
   * Reverses the bits of a 32-bit integer.
   *
   * @param n The 32-bit integer to reverse its bits.
   * @return The integer with reversed bits.
   */
  public int reverseBits(int n) {
    int reversedN = 0;

    for (int iteration = 0; iteration < 32; iteration++) {
      int LSB_Value = (n & 1);

      reversedN = (reversedN << 1) + LSB_Value;

      n >>= 1;
    }

    return reversedN;
  }
}
