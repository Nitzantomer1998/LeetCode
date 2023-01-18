def rotate(numbers: list[int], step_amount: int) -> None:
    """
    Rotating the array to the right, step_amount times

    :param numbers: List of integers
    :param step_amount: Integer represent the amount of rotates need to be done

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Activating modulo operator (%), to handle negative step_amount
    step_amount -= int(step_amount / len(numbers)) * len(numbers)

    # Assisting function for reversing array
    def reverse(start: int, end: int) -> None:
        """
        Reversing the numbers list from index start till index end

        :param start: Integer represent the start of the array
        :param end: Integer represent the end of the array
        :return: Nothing, everything happens in place

        """
        # Loop to reverse the list from index start to index end
        while start < end:
            numbers[start], numbers[end] = numbers[end], numbers[start]

            # Update the pointers
            start += 1
            end -= 1

    # Reversing the whole list
    reverse(0, len(numbers) - step_amount - 1)

    # Reversing the first step_amount elements (instead of the last)
    reverse(len(numbers) - step_amount, len(numbers) - 1)

    # Reversing back the whole list
    reverse(0, len(numbers) - 1)
