def interval_intersection(first_list: list[list[int]], second_list: list[list[int]]) -> list[list[int]]:
    """
    Finding all the existing intersection from first_list with second_list, and return it

    :param first_list: List inside list of integers, represent list of intervals
    :param second_list: List inside list of integers, represent list of intervals
    :return: All the existing intersection in first_list with second_list

    Time Complexity: o(log(n))
    Space Complexity: o(n)
    """
    # Variable to store each intersection interval we find
    intersection_solution = []

    # I & J pointers for the interval in first_list & second_list
    i = j = 0

    # Loop to traverse every cell of the lists
    while i < len(first_list) and j < len(second_list):

        # Integers storing the possible intersection values (The middle of both intervals)
        max_left = max(first_list[i][0], second_list[j][0])
        min_right = min(first_list[i][1], second_list[j][1])

        # if max left smaller than min right, we found intersection of the current intervals, add to the solution
        if max_left <= min_right:
            intersection_solution.append([max_left, min_right])

        # Updating the index of intervals for the next iteration
        # if first_list[i][1] < second_list[j][1] than move for the next i interval
        if min_right == first_list[i][1]:
            i += 1

        # if second_list[j][1] <= first_list[i][1] than move for the next j interval
        else:
            j += 1

    # Returning the amount of intersection intervals we have found
    return intersection_solution
