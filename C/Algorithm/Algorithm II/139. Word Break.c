#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

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
