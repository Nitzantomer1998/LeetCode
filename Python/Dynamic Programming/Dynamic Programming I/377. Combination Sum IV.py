def combination_sum_4(nums: list[int], target: int) -> int:
    """
    Find the number of possible combinations to form 'target', and return it

    :param nums: A list of distinct integers.
    :param target: The target integer to form using combinations of integers from 'nums'.
    :return: The number of possible combinations to form 'target'.

    Time Complexity: o(target * nums)
    Space Complexity: o(target)
    """
    # Initialize the count array with 0s
    count = [0] * (target + 1)

    # There is one way to form the target of 0
    count[0] = 1

    # Iterate over all possible targets from 1 to target
    for i in range(1, target + 1):

        # Iterate over all numbers in the array nums
        for j in nums:

            # Check if the current number j can be used to form the current target i
            if j <= i:
                # Update the number of combinations to form the current target i
                count[i] += count[i - j]

    # The number of possible combinations to form the target is stored in count[target]
    return count[target]
