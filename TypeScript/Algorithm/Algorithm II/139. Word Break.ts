function wordBreak(s: string, wordDict: string[]): boolean {
  const STRING_LENGTH: number = s.length;
  const WORDS_LENGTH: number = wordDict.length;

  const isWordMatch: boolean[] = new Array(STRING_LENGTH + 1).fill(false);
  isWordMatch[STRING_LENGTH] = true;

  for (let stringIndex: number = STRING_LENGTH - 1; stringIndex >= 0; stringIndex--) {
    for (let wordIndex: number = 0; wordIndex < WORDS_LENGTH; wordIndex++) {
      const WORD_LENGTH: number = wordDict[wordIndex].length;

      if (WORD_LENGTH + stringIndex <= STRING_LENGTH) {
        if (wordDict[wordIndex].localeCompare(s.substring(stringIndex, stringIndex + WORD_LENGTH)) === 0)
          isWordMatch[stringIndex] = isWordMatch[stringIndex + WORD_LENGTH];

        if (isWordMatch[stringIndex]) 
          break;
      }
    }
  }

  return isWordMatch[0];
}
