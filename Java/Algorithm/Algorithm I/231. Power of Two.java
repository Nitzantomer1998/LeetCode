class Solution {

  public boolean isPowerOfTwo(int n) {
    boolean isPositive = n > 0;
    boolean isTwoPower = (n & (n - 1)) == 0;

    return isPositive && isTwoPower;
  }
}
