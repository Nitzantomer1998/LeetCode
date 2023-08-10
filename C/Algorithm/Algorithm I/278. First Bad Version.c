/*
 * Finds the first bad version in a range of versions using binary search.
 *
 * The 'firstBadVersion' function identifies the first bad version within a range of
 * software versions using a binary search algorithm. It initializes two pointers,
 * 'leftPointer' and 'rightPointer', to the start and end of the version range,
 * respectively. The function repeatedly calculates the middle version using the formula
 * `(rightPointer + leftPointer) / 2`, and then calls the 'isBadVersion' API to determine
 * if the middle version is bad. If the middle version is bad, the 'rightPointer' is
 * adjusted to the middle version's left, narrowing the search range. Otherwise, the
 * 'leftPointer' is adjusted to the middle version's right, continuing the search. The
 * process continues until the search range is narrowed to a single version, which is the
 * first bad version. The function then returns the index of the first bad version.
 *
 * Parameters:
 * - n: The total number of versions to search through.
 *
 * Returns:
 * The index of the first bad version within the given range of versions.
 *
 * Note: The 'isBadVersion' API function is assumed to be defined and provided for use
 * within this function.
 *
 * This function efficiently uses binary search to identify the first bad version by
 * narrowing down the search range based on the 'isBadVersion' results. It returns the
 * index of the first bad version found.
 */
int firstBadVersion(int n) {
    int leftPointer = 1;
    int rightPointer = n;
    
    while (leftPointer <= rightPointer) {
        int middlePointer = (rightPointer + leftPointer) / 2;
        
        if (isBadVersion(middlePointer))
            rightPointer = middlePointer - 1;

        else
            leftPointer = middlePointer + 1;
    }

    return rightPointer + 1;
}
