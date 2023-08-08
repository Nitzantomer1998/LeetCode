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
