class Solution {

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
