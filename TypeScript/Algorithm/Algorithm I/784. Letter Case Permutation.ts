/**
 * Generates all possible letter case permutations of the given string.
 * @param {string} s - The input string containing letters and digits.
 * @returns {string[]} An array of strings containing all letter case permutations.
 */
function letterCasePermutation(s: string): string[] {
  const combinationArray: string[] = [];

  /**
   * Performs depth-first search (DFS) to generate letter case permutations.
   * @param {string} currentCombination - The current combination being formed.
   * @param {number} currentIndex - The index of the current character in the string.
   */
  function dfs(currentCombination: string, currentIndex: number) {
    if (currentIndex === s.length) {
      combinationArray.push(currentCombination);
      return;
    }

    if (!/[a-z]/i.test(s[currentIndex])) {
      dfs(currentCombination.concat(s[currentIndex]), currentIndex + 1);
      return;
    }

    dfs(currentCombination + s[currentIndex].toLowerCase(), currentIndex + 1);
    dfs(currentCombination + s[currentIndex].toUpperCase(), currentIndex + 1);
  }

  dfs("", 0);

  return combinationArray;
}
