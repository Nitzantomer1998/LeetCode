import random


class Solution:

    def __init__(self, numbers: list[int]):
        
        self.array = numbers[:]

    def reset(self) -> list[int]:
        
        return self.array

    def shuffle(self) -> list[int]:
        
        shuffle_array = self.array[:]

        for index in range(len(shuffle_array)):
            swap_number = random.randrange(index, len(shuffle_array))
            shuffle_array[index], shuffle_array[swap_number] = shuffle_array[swap_number], shuffle_array[index]

        return shuffle_array
