import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {

  /**
   * Given an array of integers, finds all unique triplets that sum to zero (0).
   *
   * @param nums An array of integers where triplets are to be found.
   * @return A list of lists containing unique triplets that sum to zero (0).
   */
  public List<List<Integer>> threeSum(int[] nums) {
    int NUMS_LENGTH = nums.length;

    List<List<Integer>> uniqueSolution = new ArrayList<>();

    Arrays.sort(nums);

    for (int i = 0; i < NUMS_LENGTH - 2; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) 
        continue;

      int left = i + 1;
      int right = NUMS_LENGTH - 1;

      while (left < right) {
        int currentSum = nums[i] + nums[left] + nums[right];

        if (currentSum < 0) 
          left++; 
          
        else if (currentSum > 0) 
          right--; 
        
        else {
          List<Integer> solution = new ArrayList<>();
          solution.add(nums[i]);
          solution.add(nums[left]);
          solution.add(nums[right]);
          uniqueSolution.add(solution);

          left++;

          while (left < right && nums[left] == nums[left - 1]) 
            left++;
        }
      }
    }

    return uniqueSolution;
  }
}
