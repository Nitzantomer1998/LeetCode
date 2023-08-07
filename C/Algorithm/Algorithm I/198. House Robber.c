#define MAX(X, Y) (X > Y ? X : Y)

int rob(int* nums, int numsSize) {
    for (int index = numsSize - 3; index > -1; index--) {
        int firstOption = numsSize > index + 3 ? nums[index + 3] : -1; 
        int secondOption = nums[index + 2];

        nums[index] += MAX(firstOption, secondOption);
    }

    return numsSize == 1 ? nums[0] : MAX(nums[0], nums[1]);
}
