from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that sum to zero.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[List[int]]: A list of lists containing unique triplets that sum to zero.
        """
        NUMS_LENGTH = len(nums)

        uniqueSolution = []

        nums.sort()

        for i in range(NUMS_LENGTH):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = NUMS_LENGTH - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum < 0:
                    left += 1

                elif currentSum > 0:
                    right -= 1

                else:
                    uniqueSolution.append([nums[i], nums[left], nums[right]])

                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return uniqueSolution
