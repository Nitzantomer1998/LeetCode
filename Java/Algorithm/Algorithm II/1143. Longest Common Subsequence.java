class Solution {

  public int longestCommonSubsequence(String textA, String textB) {
    int A_LENGTH = textA.length() + 1;
    int B_LENGTH = textB.length() + 1;

    int[][] commonSubsequence = new int[A_LENGTH][B_LENGTH];

    for (int row = 1; row < A_LENGTH; row++) {
      for (int column = 1; column < B_LENGTH; column++) {
        if (textA.charAt(row - 1) == textB.charAt(column - 1)) 
          commonSubsequence[row][column] = commonSubsequence[row - 1][column - 1] + 1; 
          
        else commonSubsequence[row][column] =
          Math.max(
            commonSubsequence[row - 1][column],
            commonSubsequence[row][column - 1]
          );
      }
    }

    return commonSubsequence[A_LENGTH - 1][B_LENGTH - 1];
  }
}
