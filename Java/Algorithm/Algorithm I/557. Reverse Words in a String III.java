class Solution {

  private void reverseWord(char[] s, int startPointer, int endPointer) {
    while (startPointer < endPointer) {
      char tempChar = s[startPointer];

      s[startPointer] = s[endPointer];
      s[endPointer] = tempChar;

      startPointer++;
      endPointer--;
    }
  }

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
