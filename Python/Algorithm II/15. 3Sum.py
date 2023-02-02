def three_sum(numbers: list[int]) -> list[list[int]]:
    """
    Finding all the three sum options in numbers without duplicates that equal to zero, and return them

    :param numbers: List of integers
    :return: All the three sum options in numbers without duplicates that equal to zero

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n)
    """
    # Sorting the numbers -> O(nlog(n))
    numbers.sort()

    # List storing the solutions
    three_sum_solution = []

    # Loop to traverse the numbers list
    for i in range(len(numbers) - 2):

        # if the current numbers[i] equal to the previous numbers[i - 1], then we skip in order to avoid duplications
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        # Left & Right pointers for moving on the left available indices [i + 1 ... len(numbers) - 1]
        left, right = i + 1, len(numbers) - 1

        # Loop to traverse the pointers left and right, in order to achieve the desire sum
        while left < right:

            # Storing the current sum, for more readable code
            current_sum = numbers[i] + numbers[left] + numbers[right]

            # if the current sum is larger than zero, than we need to lower the sum, therefor right moving to the left
            if current_sum > 0:
                right -= 1

            # if the current sum is lower than zero, than we need to enlarge the sum, therefor left moving to the right
            elif current_sum < 0:
                left += 1

            # if We got the desirable sum, save the solution, and update the pointers
            else:
                three_sum_solution.append([numbers[i], numbers[left], numbers[right]])

                # Update left pointer
                left += 1

                # Loop to fix the left pointer, if numbers[l] equal to numbers[l - 1] we will get duplicate solution
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1

    # Returning all the three sum options in numbers without duplicates that equal to zero
    return three_sum_solution
