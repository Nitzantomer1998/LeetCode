class Solution {

  /**
   * Checks if a given integer is a power of two.
   *
   * @param n The integer to check.
   * @return True if the integer is a power of two, otherwise false.
   */
  public boolean isPowerOfTwo(int n) {
    boolean isPositive = n > 0;
    boolean isTwoPower = (n & (n - 1)) == 0;

    return isPositive && isTwoPower;
  }
}
