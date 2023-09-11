class Solution {

  /**
   * Checks if a permutation of string s1 is contained within string s2.
   *
   * @param s1 The string to be checked for permutation.
   * @param s2 The string where the permutation of s1 is to be checked.
   * @return True if a permutation of s1 is found within s2, otherwise false.
   */
  public boolean checkInclusion(String s1, String s2) {
    int S1_LENGTH = s1.length();
    int S2_LENGTH = s2.length();

    if (S1_LENGTH > S2_LENGTH) {
      return false;
    }

    int[] stringOneContent = new int[26];
    int[] stringTwoContent = new int[26];

    for (int index = 0; index < S1_LENGTH; index++) {
      stringOneContent[s1.charAt(index) - 'a']++;
      stringTwoContent[s2.charAt(index) - 'a']++;
    }

    for (int index = S1_LENGTH; index < S2_LENGTH; index++) {
      if (Arrays.equals(stringOneContent, stringTwoContent)) {
        return true;
      }

      int charToAdd = s2.charAt(index) - 'a';
      int charToRemove = s2.charAt(index - S1_LENGTH) - 'a';

      stringTwoContent[charToAdd]++;
      stringTwoContent[charToRemove]--;
    }

    return Arrays.equals(stringOneContent, stringTwoContent);
  }
}
