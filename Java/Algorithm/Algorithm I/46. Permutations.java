class Solution {

  private void backtrack(List<List<Integer>> permutatedList, List<Integer> tempList, int[] nums) {
    int NUMS_LENGTH = nums.length;

    if (tempList.size() == NUMS_LENGTH) 
      permutatedList.add(new ArrayList<>(tempList)); 
      
    else {
      for (int index = 0; index < NUMS_LENGTH; index++) {
        if (tempList.contains(nums[index])) 
          continue;

        tempList.add(nums[index]);
        this.backtrack(permutatedList, tempList, nums);
        tempList.remove(tempList.size() - 1);
      }
    }
  }

  public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> permutatedList = new ArrayList<>();

    this.backtrack(permutatedList, new ArrayList<>(), nums);

    return permutatedList;
  }
}
