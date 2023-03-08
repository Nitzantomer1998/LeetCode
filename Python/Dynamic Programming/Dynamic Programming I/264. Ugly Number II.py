def nth_ugly_number(n: int) -> int:
    
    ugly_numbers = [0] * n
    ugly_numbers[0] = 1
    ptr2 = ptr3 = ptr5 = 0

    for i in range(1, n):
        multiple_of_2 = ugly_numbers[ptr2] * 2
        multiple_of_3 = ugly_numbers[ptr3] * 3
        multiple_of_5 = ugly_numbers[ptr5] * 5

        ugly_numbers[i] = min(multiple_of_2, multiple_of_3, multiple_of_5)

        if ugly_numbers[i] == multiple_of_2:
            ptr2 += 1
        if ugly_numbers[i] == multiple_of_3:
            ptr3 += 1
        if ugly_numbers[i] == multiple_of_5:
            ptr5 += 1

    return ugly_numbers[-1]
