def max_sub_array(numbers: list[int]) -> int:
    
    def max_sub_array(numbers: list[int]) -> int:
       
        for index in range(len(numbers) - 2, -1, -1):

            if numbers[index] + numbers[index + 1] > numbers[index]:
                numbers[index] += numbers[index + 1]

        return max(numbers)

    if len(numbers) == 1:
        return numbers[0]

    drop = max_sub_array(numbers[1:])

    pick = sum(numbers) + max(0, max_sub_array([-number for number in numbers[1:]]))

    return max(drop, pick)
