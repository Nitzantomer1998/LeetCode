/**
 * Generates all possible combinations of k numbers from 1 to n.
 * @param {number} n - The range of numbers from 1 to n.
 * @param {number} k - The number of elements in each combination.
 * @returns {number[][]} An array of arrays containing all combinations.
 */
function combine(n: number, k: number): number[][] {
  const combinationArray: number[][] = [];

  /**
   * Performs depth-first search (DFS) to generate combinations.
   * @param {number[]} currentCombination - The current combination being formed.
   * @param {number} startIndex - The index to start considering numbers from.
   */
  function dfs(currentCombination: number[], startIndex: number) {
    if (currentCombination.length === k) {
      combinationArray.push(currentCombination);
      return;
    }

    for (let index: number = startIndex; index <= n; index++)
      dfs(currentCombination.concat(index), index + 1);
  }

  dfs([], 1);

  return combinationArray;
}
