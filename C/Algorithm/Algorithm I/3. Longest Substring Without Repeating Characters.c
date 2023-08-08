/*
 * Calculates the length of the longest substring without repeating characters.
 *
 * The 'lengthOfLongestSubstring' function calculates the length of the longest substring
 * in a given string 's' that does not contain any repeating characters. It iterates
 * through the string using a sliding window approach, maintaining a substring defined by
 * 'substringStartIndex' and 'substringEndIndex'. It uses an integer array 'currentSubstring'
 * to keep track of the frequency of characters in the current substring. If a character is
 * already present in the current substring, the function slides the window by incrementing
 * 'substringStartIndex' until the repeating character is removed from the substring. The
 * function also updates the 'maxSubstringLength' variable with the length of the longest
 * non-repeating substring encountered during the iteration.
 *
 * Parameters:
 * - s: A pointer to a null-terminated string.
 *
 * Returns:
 * The length of the longest substring without repeating characters.
 *
 * This function efficiently calculates the length of the longest non-repeating substring by
 * utilizing a sliding window approach and keeping track of character frequencies. It returns
 * the length of the longest substring found in the input string 's'.
 */
int lengthOfLongestSubstring(char * s) {
    int stringLength = strlen(s);
    int maxSubstringLength = 0;
    int substringStartIndex = 0;

    int currentSubstring[512];
    memset(currentSubstring, 0, sizeof(int) * 512);
    
    for (int substringEndIndex = 0; substringEndIndex < stringLength; substringEndIndex++) {
        int charIndex = s[substringEndIndex];

        if (currentSubstring[charIndex]) {
            assert(currentSubstring[charIndex] == 1);

            while (substringStartIndex < substringEndIndex) {
                int decreaseIndex = s[substringStartIndex];
                currentSubstring[decreaseIndex]--;
                substringStartIndex++;

                if (currentSubstring[charIndex] == 0)
                    break;
            }
        }

        currentSubstring[charIndex]++;
        maxSubstringLength = MAX(maxSubstringLength, substringEndIndex - substringStartIndex + 1);
    }

    return maxSubstringLength;
}
