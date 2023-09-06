public class Solution {

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
