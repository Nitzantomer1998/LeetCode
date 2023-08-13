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
