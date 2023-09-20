function longestCommonSubsequence(textA: string, textB: string): number {
  const A_LENGTH: number = textA.length + 1;
  const B_LENGTH: number = textB.length + 1;

  const commonSubsequence: number[][] = Array.from({ length: A_LENGTH }, () => Array(B_LENGTH).fill(0));

  for (let row: number = 1; row < A_LENGTH; row++) {
    for (let column: number = 1; column < B_LENGTH; column++) {
      if (textA[row - 1] === textB[column - 1])
        commonSubsequence[row][column] = commonSubsequence[row - 1][column - 1] + 1;
      
      else
        commonSubsequence[row][column] = Math.max(commonSubsequence[row - 1][column], commonSubsequence[row][column - 1]);
    }
  }

  return commonSubsequence[A_LENGTH - 1][B_LENGTH - 1];
}
