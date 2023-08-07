/* Definition for getting the maximum value */
#define MAX(X, Y) (X > Y ? X : Y)

/*
 * Determines the maximum amount that can be robbed from a row of houses.
 *
 * The 'rob' function calculates the maximum amount that can be robbed from a row of
 * houses, where each house contains a certain amount of money. It employs dynamic
 * programming to iteratively calculate the maximum amount that can be robbed at each
 * house. The function starts from the end of the house row and works backwards,
 * considering two options for each house: robbing the current house along with the
 * houses at least two positions away, or skipping the current house and robbing the
 * house at the next position. The calculated values are stored in the 'nums' array.
 * Finally, the function returns the maximum amount that can be robbed from the first
 * two houses or the first house, depending on the number of houses.
 *
 * Parameters:
 * - nums: A pointer to an array of integers representing the amounts of money in each house.
 * - numsSize: The number of houses in the row.
 *
 * Returns:
 * The maximum amount that can be robbed from the row of houses.
 *
 * This function efficiently calculates the maximum amount that can be robbed by
 * considering two options for each house and storing the calculated values in the 'nums'
 * array. It returns the maximum amount that can be robbed from the given house row.
 */
int rob(int* nums, int numsSize) {
    for (int index = numsSize - 3; index > -1; index--) {
        int firstOption = numsSize > index + 3 ? nums[index + 3] : -1; 
        int secondOption = nums[index + 2];

        nums[index] += MAX(firstOption, secondOption);
    }

    return numsSize == 1 ? nums[0] : MAX(nums[0], nums[1]);
}
