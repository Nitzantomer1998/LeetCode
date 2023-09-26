#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

/*
 * Determines if a string can be segmented into words from a word dictionary.
 *
 * The 'wordBreak' function takes an input string 's', an array of words 'wordDict', and the size
 * of the word dictionary 'wordDictSize' as input. It checks if the input string 's' can be segmented
 * into words from the given word dictionary. It uses dynamic programming to track whether substrings
 * of 's' can be formed using words from the dictionary.
 *
 * Parameters:
 * - s: The input string to be segmented.
 * - wordDict: An array of words from the dictionary.
 * - wordDictSize: The number of words in the dictionary.
 *
 * Returns:
 * 'true' if 's' can be segmented into words from the dictionary, 'false' otherwise.
 */
bool wordBreak(char *s, char **wordDict, int wordDictSize)
{
  int STRING_LENGTH = strlen(s);
  int WORDS_LENGTH = wordDictSize;

  bool *isWordMatch = (bool *)malloc((STRING_LENGTH + 1) * sizeof(bool));
  memset(isWordMatch, false, (STRING_LENGTH + 1) * sizeof(bool));
  isWordMatch[0] = true;

  for (int i = 1; i <= STRING_LENGTH; i++)
  {
    for (int j = 0; j < WORDS_LENGTH; j++)
    {
      int WORD_LENGTH = strlen(wordDict[j]);

      if (i >= WORD_LENGTH && isWordMatch[i - WORD_LENGTH] && strncmp(s + i - WORD_LENGTH, wordDict[j], WORD_LENGTH) == 0)
      {
        isWordMatch[i] = true;
        break;
      }
    }
  }

  bool result = isWordMatch[STRING_LENGTH];
  free(isWordMatch);

  return result;
}
