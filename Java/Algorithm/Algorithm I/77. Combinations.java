class Solution {

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

  public List<List<Integer>> combine(int n, int k) {
    List<List<Integer>> combinations = new ArrayList<>();
    List<Integer> digits = new ArrayList<>();

    for (int digit = 1; digit <= n; digit++) 
      digits.add(digit);

    createCombinations(combinations, new ArrayList<>(), digits, k, 0);

    return combinations;
  }
}
