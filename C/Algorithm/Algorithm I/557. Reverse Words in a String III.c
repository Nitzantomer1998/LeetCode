/*
 * Swaps two characters within a string.
 *
 * The 'swapChar' function takes two pointers to characters 'charA' and 'charB' as input
 * and swaps their values. It uses a temporary variable 'temp' to store the value of
 * 'charA', then assigns the value of 'charB' to 'charA' and finally assigns the stored
 * value of 'charA' to 'charB'. After the function is executed, the characters at 'charA'
 * and 'charB' are effectively swapped within the string.
 *
 * Parameters:
 * - charA: A pointer to the first character to be swapped.
 * - charB: A pointer to the second character to be swapped.
 *
 * This function performs an in-place swap of two characters within a string, effectively
 * swapping the contents of the memory locations pointed to by 'charA' and 'charB'.
 */
void swapChar(char* charA, char* charB) {
    char temp = *charA;

    *charA = *charB;
    *charB = temp;
}

/*
 * Reverses a word within a string.
 *
 * The 'reverseWord' function reverses a word within the string 'string' starting from
 * 'startPointer' to 'endPointer'. It uses the 'swapChar' function to swap characters
 * while moving the 'startPointer' towards the 'endPointer' and vice versa. This
 * effectively reverses the word within the string.
 *
 * Parameters:
 * - string: A pointer to the string containing the word to be reversed.
 * - startPointer: The index of the first character of the word.
 * - endPointer: The index of the last character of the word.
 *
 * This function performs an in-place reversal of a word within the string by swapping
 * characters from both ends of the word and moving towards the center.
 */
void reverseWord(char* string, int startPointer, int endPointer) {
    while (startPointer < endPointer) {
        swapChar(string + startPointer, string + endPointer);

        startPointer++;
        endPointer--;
    }
}

/*
 * Reverses each word in a string.
 *
 * The 'reverseWords' function takes a string 's' as input and reverses each word within
 * the string. It iterates through the string and identifies word boundaries based on
 * spaces. For each word found, the 'reverseWord' function is called to reverse the word
 * in-place. The resulting modified string is returned.
 *
 * Parameters:
 * - s: A pointer to the input string to be processed.
 *
 * Returns:
 * A pointer to the modified string with each word reversed.
 *
 * This function efficiently reverses each word within the input string in-place by using
 * the 'reverseWord' function and swapping characters to achieve the desired reversal.
 */
char * reverseWords(char * s) {
    int stringLength = strlen(s);
    int wordStartIndex = 0;

    for (int wordEndIndex = 0; wordEndIndex < stringLength + 1; wordEndIndex++)
        if (wordEndIndex == stringLength || s[wordEndIndex] == ' ') {
            reverseWord(s, wordStartIndex, wordEndIndex - 1);
            wordStartIndex = wordEndIndex + 1;
        }

    return s;
}
