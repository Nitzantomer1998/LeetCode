class Solution:
    def climb_stairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb to the top of a staircase with 'n' steps.

        Args:
            n (int): An integer representing the total number of steps in the staircase.
        
        Returns:
            bool: The number of distinct ways to reach the top.

        Time Complexity: o(n) where n is the number of steps in the staircase.
        Space Complexity: o(1) since we only use two integers variables.
        """
        current_option = 1
        previous_option = 0

        for _ in range(n):
            current_option, previous_option = current_option + previous_option, current_option

        return current_option
