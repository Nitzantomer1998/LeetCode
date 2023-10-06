from typing import List

class Solution:
    def generatePermute(self, permutations: List[List[int]], currentPermute: List[int], nums: List[int], used: List[bool]) -> None:
        """
        Generate all possible permutations of a list of integers using backtracking.

        Args:
            permutations (List[List[int]]): A list to store the generated permutations.
            currentPermute (List[int]): The current permutation being constructed.
            nums (List[int]): The input list of integers.
            used (List[bool]): A list to track used elements during the generation process.

        Returns:
            None: The function modifies the 'permutations' list in-place.

        Time Complexity: o(n * n!) where n is the length of the input list.
        Space Complexity: o(n * n!) where n is the length of the input list.
        """
        if len(currentPermute) == len(nums):
            permutations.append(currentPermute.copy())
            return

        for index, value in enumerate(nums):
            if not used[index]:
                used[index] = True
                currentPermute.append(value)
                self.generatePermute(permutations, currentPermute, nums, used)
                used[index] = False
                currentPermute.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of a list of integers.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[List[int]]: A list containing all possible permutations.
        """
        permutations = []
        used = [False] * len(nums)
        self.generatePermute(permutations, [], nums, used)
        return permutations
