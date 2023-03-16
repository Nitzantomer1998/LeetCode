def length_of_LIS(numbers: list[int]) -> int:
    
    LIS = [1] * len(numbers)

    for i in range(len(numbers) - 1, -1, -1):

        for j in range(i + 1, len(numbers)):

            if numbers[i] < numbers[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    return max(LIS)
