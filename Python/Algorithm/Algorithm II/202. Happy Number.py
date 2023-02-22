def is_happy(n: int) -> bool:
    """
    Finding if n is a happy number, and return accordingly
    Happy number : replace the number by the sum of the squares of its digits, repeat process till number is 1

    :param n: Integer
    :return: True if n is a happy number, else False

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Set storing every output calculation, in order to prevent situation of infinite loop
    seen = set()

    # Loop to calculate if the number is happy or not
    # Note : Loop is deactivate when the number is happy, or we re-visit an old calculation (entering a cycle)
    while n != 1 and n not in seen:

        # Updating the seen Set to include the current value
        seen.add(n)

        # Calculating the next value
        current_sum = 0
        while n > 0:
            # n = n // 10, and digit = n % 10
            n, digit = divmod(n, 10)

            # Updating the current sum
            current_sum += digit ** 2

        # Updating n to store the new calculation, for the new iteration
        n = current_sum

    # Returning True if n equal to 1, else False
    return n == 1
