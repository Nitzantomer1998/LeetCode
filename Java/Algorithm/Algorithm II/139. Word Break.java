class Solution {

  /**
   * Determines if a given string can be segmented into words from the word dictionary.
   *
   * @param s         The input string to be segmented.
   * @param wordDict  A list of words in the dictionary.
   * @return True if the input string can be segmented into words from the dictionary; otherwise, false.
   */
  public boolean wordBreak(String s, List<String> wordDict) {
    int STRING_LENGTH = s.length();
    int WORDS_LENGTH = wordDict.size();

    boolean[] isWordMatch = new boolean[STRING_LENGTH + 1];
    isWordMatch[STRING_LENGTH] = true;

    for (int stringIndex = STRING_LENGTH - 1; stringIndex >= 0; stringIndex--) {
      for (int wordIndex = 0; wordIndex < WORDS_LENGTH; wordIndex++) {
        int WORD_LENGTH = wordDict.get(wordIndex).length();

        if (WORD_LENGTH + stringIndex <= STRING_LENGTH) {
          if (wordDict.get(wordIndex).equals(s.substring(stringIndex, stringIndex + WORD_LENGTH))) 
            isWordMatch[stringIndex] = isWordMatch[stringIndex + WORD_LENGTH];

          if (isWordMatch[stringIndex]) 
            break;
        }
      }
    }

    return isWordMatch[0];
  }
}
