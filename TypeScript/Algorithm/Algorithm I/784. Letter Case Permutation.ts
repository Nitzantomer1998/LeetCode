function letterCasePermutation(s: string): string[] {
  const combinationArray: string[] = [];

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
