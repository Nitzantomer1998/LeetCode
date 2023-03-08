def nth_ugly_number(n: int) -> int:
    """
    Generates and returns the nth ugly number, where an ugly number is a positive integer whose prime factors are limited
    to 2, 3, and 5.

    :param n: The nth ugly number to generate.
    :return: The nth ugly number.

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # initialize array to store generated ugly numbers
    ugly_numbers = [0] * n
    # first ugly number is 1
    ugly_numbers[0] = 1
    # pointers to track multiples of 2, 3 and 5
    ptr2 = ptr3 = ptr5 = 0

    # generate n ugly numbers
    for i in range(1, n):
        # calculate multiples of 2, 3 and 5 using pointers
        multiple_of_2 = ugly_numbers[ptr2] * 2
        multiple_of_3 = ugly_numbers[ptr3] * 3
        multiple_of_5 = ugly_numbers[ptr5] * 5

        # choose the smallest multiple as the next ugly number
        ugly_numbers[i] = min(multiple_of_2, multiple_of_3, multiple_of_5)

        # update pointers if the chosen multiple is the same as the corresponding ugly number
        if ugly_numbers[i] == multiple_of_2:
            ptr2 += 1
        if ugly_numbers[i] == multiple_of_3:
            ptr3 += 1
        if ugly_numbers[i] == multiple_of_5:
            ptr5 += 1

    # return the last generated ugly number
    return ugly_numbers[-1]
