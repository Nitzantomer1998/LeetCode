int climbStairs(int n) {
    int prevStairsOptions = 0;
    int currentStairsOptions = 1;

    for (int index = 0; index < n; index++) {
        int temp = currentStairsOptions;

        currentStairsOptions += prevStairsOptions;
        prevStairsOptions = temp;
    }

    return currentStairsOptions;
}
