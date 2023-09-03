function sortedSquares(nums: number[]): number[] {
  const numsLength: number = nums.length;
  const squareSortArray: number[] = new Array(numsLength);

  let leftPointer: number = 0;
  let rightPointer: number = numsLength - 1;

  for (let index: number = numsLength - 1; index >= 0; index--) {
    const squareStart: number = nums[leftPointer] ** 2;
    const squareEnd: number = nums[rightPointer] ** 2;

    squareSortArray[index] = squareEnd > squareStart ? squareEnd : squareStart;

    if (squareEnd > squareStart) rightPointer--;
    else leftPointer++;
  }

  return squareSortArray;
}
