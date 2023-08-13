/*
 * Checks if one string is a permutation of another within a larger string.
 *
 * The 'checkInclusion' function determines whether the characters of string 's1' can
 * be rearranged to form a substring of string 's2'. It uses a sliding window approach
 * to maintain a window of characters from 's2' that has the same length as 's1'. The
 * window's current content is tracked using the 'windowCurrentContent' array, which
 * stores the frequency of characters within the current window. The variable
 * 'missMatchChars' is used to count the characters that do not match between 's1' and
 * the current window. The function iterates through the characters of 's1' and
 * initializes the 'windowCurrentContent' accordingly. It then slides the window over
 * 's2', adjusting the character counts in the 'windowCurrentContent' array. If all
 * characters in 's1' are matched within the window, 'missMatchChars' becomes zero,
 * indicating a successful permutation, and the function returns true.
 *
 * Parameters:
 * - s1: A pointer to the string to be checked for permutation.
 * - s2: A pointer to the larger string in which the permutation is sought.
 *
 * Returns:
 * 'true' if 's1' is a permutation of a substring within 's2', 'false' otherwise.
 *
 * This function efficiently determines whether one string is a permutation of another
 * string within a larger string using a sliding window and character frequency tracking.
 */
bool checkInclusion(char *s1, char *s2) {
    int stringOneLength = strlen(s1);
    int stringTwoLength = strlen(s2);

    int windowCurrentContent[26] = {0};
    int missMatchChars = 0;

    if (stringOneLength > stringTwoLength)
        return false;

    for (int index = 0; index < stringOneLength; index++) {
        windowCurrentContent[s1[index] - 'a']++;
        windowCurrentContent[s2[index] - 'a']--;
    }

    for (int index = 0; index < 26; index++)
        if (windowCurrentContent[index] != 0)
            missMatchChars++;

    if (missMatchChars == 0)
        return true;

    for (int index = stringOneLength; index < stringTwoLength; index++) {
        windowCurrentContent[s2[index] - 'a']--;

        if (windowCurrentContent[s2[index] - 'a'] == 0)
            missMatchChars--;
        
        else if (windowCurrentContent[s2[index] - 'a'] == -1)
            missMatchChars++;

        windowCurrentContent[s2[index - stringOneLength] - 'a']++;

        if (windowCurrentContent[s2[index - stringOneLength] - 'a'] == 0)
            missMatchChars--;

        else if (windowCurrentContent[s2[index - stringOneLength] - 'a'] == 1)
            missMatchChars++;

        if (missMatchChars == 0)
            return true;
    }

    return false;
}
