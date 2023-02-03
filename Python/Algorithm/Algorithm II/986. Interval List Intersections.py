def interval_intersection(first_list: list[list[int]], second_list: list[list[int]]) -> list[list[int]]:
    
    intersection_solution = []

    i = j = 0

    while i < len(first_list) and j < len(second_list):

        max_left = max(first_list[i][0], second_list[j][0])
        min_right = min(first_list[i][1], second_list[j][1])

        if max_left <= min_right:
            intersection_solution.append([max_left, min_right])

        if min_right == first_list[i][1]:
            i += 1

        else:
            j += 1

    return intersection_solution
