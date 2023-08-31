function combine(n: number, k: number): number[][] {
  const combinationArray: number[][] = [];

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
