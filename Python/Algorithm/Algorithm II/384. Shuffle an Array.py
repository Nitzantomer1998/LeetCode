import random


class Solution:

    def __init__(self, numbers: list[int]):
        """
        Initialize the instance with attribute array

        :param numbers: List of integers, initialize with Deep Copy

        Time Complexity: o(n)
        Space Complexity: o(n)
        """
        self.array = numbers[:]

    def reset(self) -> list[int]:
        """
        Reset the array to be the original, and return it

        :return: The original array

        Time Complexity: o(1)
        Space Complexity: o(1)
        """
        return self.array

    def shuffle(self) -> list[int]:
        """
        Creating random shuffle from attribute array, and return it

        :return: Returns a random shuffling of the array

        Time Complexity: o(n)
        Space Complexity: o(n)
        """
        # Using deep copy, so we won't affect the original array
        shuffle_array = self.array[:]

        # Loop to make a shuffle array
        for index in range(len(shuffle_array)):
            # Making indices swap using random functions, AKA the Fisher-Yates Algorithm
            swap_number = random.randrange(index, len(shuffle_array))
            shuffle_array[index], shuffle_array[swap_number] = shuffle_array[swap_number], shuffle_array[index]

        # Returns random shuffle of the array
        return shuffle_array
