# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def first_bad_version(version_list_size: int) -> int:
    """
    Finding the first bad version in our "product", and return it index

    :param version_list_size: Integer represent amount of existed version for the product
    :return: The index of the first bad version in our "product"

    Time Complexity: o(log(n))
    Space Complexity: o(1)
    """
    # Variable to the solution
    first_bad_version_solution = 1

    # Pointers to current container we are searching at
    left, right = 1, version_list_size

    # Loop to traverse the existed versions without repeating
    while left <= right:

        # Variable to store the middle of the current container we are searching at
        middle = (right + left) // 2

        # if we found bad version
        if isBadVersion(middle):

            # Update the current solution
            first_bad_version_solution = middle

            # Update the current container and keep searching for earlier bad versions
            right = middle - 1

        # if we haven't found bad version, then the version container
        else:
            left = middle + 1

    # Returning the solution
    return first_bad_version_solution
