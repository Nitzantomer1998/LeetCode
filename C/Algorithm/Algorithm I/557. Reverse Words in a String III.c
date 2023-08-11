void swapChar(char* charA, char* charB) {
    char temp = *charA;

    *charA = *charB;
    *charB = temp;
}

void reverseWord(char* string, int startPointer, int endPointer) {
    while (startPointer < endPointer) {
        swapChar(string + startPointer, string + endPointer);

        startPointer++;
        endPointer--;
    }
}
