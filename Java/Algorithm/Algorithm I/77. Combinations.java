class Solution {

  /**
   * Recursively generates combinations of integers.
   *
   * @param combinations       The list to store generated combinations.
   * @param currentCombination The current combination being constructed.
   * @param digits             The list of available digits to choose from.
   * @param permuteSize        The size of combinations to generate.
   * @param startIndex         The starting index within the 'digits' list.
   */
  private void createCombinations(List<List<Integer>> combinations, List<Integer> currentCombination, List<Integer> digits, int permuteSize, int startIndex) {
    if (permuteSize == 0) {
      combinations.add(new ArrayList<>(currentCombination));
      return;
    }

    for (int index = startIndex; index < digits.size(); index++) {
      int digit = digits.get(index);

      currentCombination.add(digit);
      createCombinations(combinations, currentCombination, digits, permuteSize - 1, index + 1);
      currentCombination.remove(currentCombination.size() - 1);
    }
  }

  /**
   * Generates combinations of integers from 1 to n with a given size k.
   *
   * @param n The range of integers (1 to n).
   * @param k The size of combinations to generate.
   * @return A list of combinations of size k.
   */
  public List<List<Integer>> combine(int n, int k) {
    List<List<Integer>> combinations = new ArrayList<>();
    List<Integer> digits = new ArrayList<>();

    for (int digit = 1; digit <= n; digit++) 
      digits.add(digit);

    createCombinations(combinations, new ArrayList<>(), digits, k, 0);

    return combinations;
  }
}
