class Solution {

  /**
   * Checks if a character is an alphabetical character.
   *
   * @param character The character to check.
   * @return True if the character is alphabetical, otherwise false.
   */
  private boolean isAlphabeticalCharacter(char character) {
    return character >= 'A' && character <= 'z';
  }

  /**
   * Generates all possible letter case permutations of a given string.
   *
   * @param permutations    The list to store the generated permutations.
   * @param currentPermute The current permutation being built.
   * @param s               The input string to generate permutations for.
   * @param index           The current index in the input string.
   */
  private void createPermute(List<String> permutations, StringBuilder currentPermute, String s, int index) {
    if (currentPermute.length() == s.length()) {
      permutations.add(currentPermute.toString());
      return;
    }

    char character = s.charAt(index);

    if (isAlphabeticalCharacter(character)) {
      currentPermute.append(Character.toLowerCase(character));
      createPermute(permutations, currentPermute, s, index + 1);
      currentPermute.deleteCharAt(currentPermute.length() - 1);

      currentPermute.append(Character.toUpperCase(character));
      createPermute(permutations, currentPermute, s, index + 1);
      currentPermute.deleteCharAt(currentPermute.length() - 1);
    } 
    
    else {
      currentPermute.append(character);
      createPermute(permutations, currentPermute, s, index + 1);
      currentPermute.deleteCharAt(currentPermute.length() - 1);
    }
  }

  /**
   * Generates all possible letter case permutations of a given string.
   *
   * @param s The input string to generate permutations for.
   * @return A list of all possible letter case permutations of the input string.
   */
  public List<String> letterCasePermutation(String s) {
    List<String> permutations = new ArrayList<>();
    
    createPermute(permutations, new StringBuilder(), s, 0);
    
    return permutations;
  }
}
