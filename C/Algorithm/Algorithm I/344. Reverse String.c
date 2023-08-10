void swapChars(char* charA, char* charB) {
    char temp = *charA;

    *charA = *charB;
    *charB = temp;
}

void reverseString(char* s, int sSize) {
    int leftPointer = 0;
    int rightPointer = sSize - 1;

    while (leftPointer < rightPointer) {
        swapChars(s + leftPointer, s + rightPointer);
        leftPointer++;
        rightPointer--;
    }
}
