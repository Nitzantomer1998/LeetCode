const solution = function(isBadVersion: any) {

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
