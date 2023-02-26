from collections import Counter


def delete_and_earn(numbers: list[int]) -> int:
    """
    Find the maximum number of points you can earn by applying the operation countless times, and return it
    Operations : Pick any numbers[i] and delete it to earn numbers[i] points.
                 Afterwards, you must delete every element equal to numbers[i] - 1 or + 1
    :param numbers: List of integers
    :return: The maximum number of points you can earn by applying the operation some number of times

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Storing the duplicates amount for each number in numbers
    counter = Counter(numbers)

    # Updating numbers, to be sorted and without duplicates
    numbers = sorted(list(set(numbers)))

    # Integers holding the
    previous_earn = max_earn = 0

    # Loop to traverse each cell in numbers, and assemble the solution
    for index, value in enumerate(numbers):

        current_earn = numbers[index] * counter[value]

        # Can't add the previous earn (integers adjacent)
        if index > 0 and numbers[index] == numbers[index - 1] + 1:

            # Updating max_earn in case the current earn + previous earn is higher
            previous_earn, max_earn = max_earn, max(current_earn + previous_earn, max_earn)

        # Able to add the current earn with the max_earn
        else:

            # Updating max_earn
            previous_earn, max_earn = max_earn, current_earn + max_earn

    # Returning the final max earn
    return max_earn
