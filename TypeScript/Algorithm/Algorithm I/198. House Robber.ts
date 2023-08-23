/**
 * Returns the maximum of two numbers.
 * @param {number} valueA - The first number.
 * @param {number} valueB - The second number.
 * @returns {number} The larger of the two input numbers.
 */
function maxValue(valueA: number, valueB: number): number {
    return valueA > valueB ? valueA : valueB;
}

/**
 * Determines the maximum amount that can be robbed from a row of houses, considering certain constraints.
 * @param {number[]} nums - An array of integers representing the amounts in each house.
 * @returns {number} The maximum amount that can be robbed without robbing adjacent houses.
 */
function rob(nums: number[]): number {
    const numsLength: number = nums.length;

    for (let index: number = numsLength - 3; index >= 0; index--) {
        let firstOption: number = numsLength > index + 3 ? nums[index + 3] : 0;
        let secondOption: number = numsLength > index + 2 ? nums[index + 2] : 0;

        nums[index] += maxValue(firstOption, secondOption);
    }

    return numsLength === 1 ? nums[0] : maxValue(nums[0], nums[1]);
};
