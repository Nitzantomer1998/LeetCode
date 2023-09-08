class Solution {

  /**
   * Calculates the length of the longest substring without repeating characters in a given string.
   *
   * @param s The input string.
   * @return The length of the longest substring without repeating characters.
   */
  public int lengthOfLongestSubstring(String s) {
    Map<Character, Integer> windowContext = new HashMap<>();
    int STRING_LENGTH = s.length();
    int longestSubstring = 0;
    int startPointer = 0;

    for (int endPointer = 0; endPointer < STRING_LENGTH; endPointer++) {
      char currentChar = s.charAt(endPointer);

      if (windowContext.containsKey(currentChar) == false || windowContext.get(currentChar) < startPointer) {
        windowContext.put(currentChar, endPointer);
        longestSubstring = Math.max(longestSubstring, endPointer - startPointer + 1);
      } 
      
      else {
        startPointer = windowContext.get(currentChar) + 1;
        windowContext.put(currentChar, endPointer);
      }
    }

    return longestSubstring;
  }
}
