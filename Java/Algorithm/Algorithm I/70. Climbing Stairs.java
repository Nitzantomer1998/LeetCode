class Solution {

  /**
   * Computes the number of distinct ways to climb to the top of n steps.
   *
   * @param n The total number of steps to climb.
   * @return The number of distinct ways to reach the top.
   */
  public int climbStairs(int n) {
    int previousStep = 0;
    int currentStep = 1;

    for (int stepIteration = 1; stepIteration <= n; stepIteration++) {
      int nextStep = previousStep + currentStep;

      previousStep = currentStep;
      currentStep = nextStep;
    }

    return currentStep;
  }
}
