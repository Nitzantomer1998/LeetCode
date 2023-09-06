public class Solution {

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
