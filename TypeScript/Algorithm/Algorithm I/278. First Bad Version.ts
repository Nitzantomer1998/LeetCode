/**
 * Represents a solution to find the first bad version using binary search.
 * @param {function} isBadVersion - A function that determines if a given version is bad.
 * @returns {function} A function that returns the first bad version.
 */
var solution = function(isBadVersion: any) {

    return function(n: number): number {
        let leftPointer: number = 1;
        let rightPointer: number = n;

        while (leftPointer <= rightPointer) {
            let middlePointer: number = Math.floor((leftPointer + rightPointer) / 2);

            if (isBadVersion(middlePointer))
                rightPointer = middlePointer - 1;

            else
                leftPointer = middlePointer + 1;
        }

        return rightPointer + 1;
    };
};
