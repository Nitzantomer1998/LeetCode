def find_number_of_LIS(numbers: list[int]) -> int:
    
    LIS = [1] * len(numbers)

    SLC = [1] * len(numbers)

    for i in range(len(numbers)):

        for j in range(i):

            if numbers[i] > numbers[j]:

                if LIS[i] < LIS[j] + 1:
                    LIS[i] = LIS[j] + 1
                    SLC[i] = SLC[j]

                elif LIS[i] == LIS[j] + 1:
                    SLC[i] += SLC[j]

    max_length = max(LIS)

    return sum(count for length, count in zip(LIS, SLC) if length == max_length)
