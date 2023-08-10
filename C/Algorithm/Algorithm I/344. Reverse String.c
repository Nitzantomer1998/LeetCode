/*
 * Swaps the values of two characters.
 *
 * The 'swapChars' function takes two pointers to characters 'charA' and 'charB' as input
 * and swaps their values. It uses a temporary variable 'temp' to store the value of
 * 'charA', then assigns the value of 'charB' to 'charA' and finally assigns the stored
 * value of 'charA' to 'charB'. After the function is executed, the values of 'charA' and
 * 'charB' are effectively swapped.
 *
 * Parameters:
 * - charA: A pointer to the first character to be swapped.
 * - charB: A pointer to the second character to be swapped.
 *
 * This function performs an in-place swap of two character values, effectively swapping
 * the contents of the memory locations pointed to by 'charA' and 'charB'.
 */
void swapChars(char* charA, char* charB) {
    char temp = *charA;

    *charA = *charB;
    *charB = temp;
}

/*
 * Reverses a string in-place.
 *
 * The 'reverseString' function takes a pointer to a character array 's' and its size
 * 'sSize' as input, and reverses the order of its characters in-place. It initializes
 * 'leftPointer' to point to the first character and 'rightPointer' to point to the last
 * character of the string. The function repeatedly swaps the characters pointed to by
 * 'leftPointer' and 'rightPointer' using the 'swapChars' function, then increments
 * 'leftPointer' and decrements 'rightPointer' to move towards the center of the string.
 * This process continues until 'leftPointer' is no longer less than 'rightPointer', and
 * the entire string is reversed.
 *
 * Parameters:
 * - s: A pointer to the character array (string) to be reversed.
 * - sSize: The size of the character array 's'.
 *
 * This function efficiently reverses the order of characters in the string by swapping
 * characters from the outer edges of the string and moving towards the center.
 */
void reverseString(char* s, int sSize) {
    int leftPointer = 0;
    int rightPointer = sSize - 1;

    while (leftPointer < rightPointer) {
        swapChars(s + leftPointer, s + rightPointer);
        leftPointer++;
        rightPointer--;
    }
}
