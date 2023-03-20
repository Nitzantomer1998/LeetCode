def integer_break(n: int) -> int:
    """
    Breaking integer n into sum of k positive integers, where 1 <= k < n and find the maximum product, and return it
    Note : Product is a multiplication of all the K you took

    :param n: Integer
    :return: The maximum product you can get

    Time Complexity: o(n * n)
    Space Complexity: o(n)
    """
    # Initialize MP with default value of index itself as its highest amount of coins, MP -> Maximum Product
    # Note : Each cell [i] will store the maximum product for the value i
    MP = [value for value in range(n + 1)]
    MP[-1] = 0

    # Double loop to traverse finding for each cell the maximum product
    for number in range(2, n + 1):
        for index in range(1, number):
            MP[number] = max(MP[number], MP[index] * MP[number - index])

    # Returning the maximum product we can get
    return MP[-1]
