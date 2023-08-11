/**
 * Calculates the number of distinct ways to climb a staircase with 'n' steps.
 *
 * The 'climbStairs' function calculates the number of distinct ways to reach the
 * top of a staircase with 'n' steps by taking one or two steps at a time. It uses
 * a dynamic programming approach, iteratively updating the number of ways based on
 * the previous steps taken. The final count of distinct ways is returned.
 *
 * Parameters:
 * - n: The total number of steps in the staircase.
 *
 * Returns:
 * The number of distinct ways to climb the staircase with 'n' steps.
 */
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
