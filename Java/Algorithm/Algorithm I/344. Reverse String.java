class Solution {

  /**
   * Reverses a character array in place.
   *
   * @param s The character array to be reversed.
   */
  public void reverseString(char[] s) {
    int STRING_LENGTH = s.length;

    int startPointer = 0;
    int endPointer = STRING_LENGTH - 1;

    while (startPointer < endPointer) {
      char tempChar = s[startPointer];

      s[startPointer] = s[endPointer];
      s[endPointer] = tempChar;

      startPointer++;
      endPointer--;
    }
  }
}
