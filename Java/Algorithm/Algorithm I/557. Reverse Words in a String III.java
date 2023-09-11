class Solution {

  /**
   * Reverses a word in a character array between the specified start and end pointers.
   *
   * @param s            The character array containing the word to be reversed.
   * @param startPointer The starting index of the word to be reversed.
   * @param endPointer   The ending index of the word to be reversed.
   */
  private void reverseWord(char[] s, int startPointer, int endPointer) {
    while (startPointer < endPointer) {
      char tempChar = s[startPointer];

      s[startPointer] = s[endPointer];
      s[endPointer] = tempChar;

      startPointer++;
      endPointer--;
    }
  }

  /**
   * Reverses the words in a string while maintaining the order of words.
   *
   * @param s The input string containing words separated by spaces.
   * @return The string with words reversed.
   */
  public String reverseWords(String s) {
    char[] characters = s.toCharArray();
    int CHARS_LENGTH = characters.length;

    int startPointer = 0;

    for (int endPointer = 0; endPointer <= CHARS_LENGTH; endPointer++) {
      if (endPointer == CHARS_LENGTH || characters[endPointer] == ' ') {
        reverseWord(characters, startPointer, endPointer - 1);
        startPointer = endPointer + 1;
      }
    }

    return new String(characters);
  }
}
