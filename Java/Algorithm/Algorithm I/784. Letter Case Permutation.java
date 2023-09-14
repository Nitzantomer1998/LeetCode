class Solution {

  private boolean isAlphabeticalCharacter(char character) {
    return character >= 'A' && character <= 'z';
  }

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

  public List<String> letterCasePermutation(String s) {
    List<String> permutations = new ArrayList<>();
    
    createPermute(permutations, new StringBuilder(), s, 0);
    
    return permutations;
  }
}
