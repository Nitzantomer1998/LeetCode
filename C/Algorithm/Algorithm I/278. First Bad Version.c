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
