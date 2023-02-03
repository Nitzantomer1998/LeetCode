def is_power_of_two(number: int) -> bool:
    """
    Checking if number is a power of two, if yes return True, else return False

    :param number: Unsigned Integer
    :return: True if number is power of 2, else False

    Time Complexity: o(1)
    Space Complexity: o(1)
    """
    # Returning whether the number is power of 2
    # Note : & operator performs bit by bit AND operation on the two values, if both bits equals 1 then output 1, else 0
    # Special case to detect if number is power be by checking if number & (number - 1) equal to 0
    return number > 0 and number & (number - 1) == 0
