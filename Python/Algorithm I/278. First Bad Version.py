def first_bad_version(version_list_size: int) -> int:
    first_bad_version_solution = 1

    left, right = 1, version_list_size

    while left <= right:

        middle = (right + left) // 2

        if isBadVersion(middle):

            first_bad_version_solution = middle

            right = middle - 1

        else:
            left = middle + 1

    return first_bad_version_solution
