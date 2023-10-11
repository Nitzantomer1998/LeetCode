from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determine the maximum amount of money that can be robbed without alerting the police.

        Args:
            nums (List[int]): A list of non-negative integers representing the amount of money in each house.

        Returns:
            int: The maximum amount of money that can be robbed.

        Time Complexity: o(n) where n is the number of houses.
        Space Complexity: o(1) since we are not using any additional space.
        """
        NUMS_LENGTH = len(nums)
        nums.append(0)

        for index in range(NUMS_LENGTH - 3, -1, -1):
            firstOption = nums[index + 3]
            secondOption = nums[index + 2]

            nums[index] += max(firstOption, secondOption)

        return max(nums[0], nums[1])
