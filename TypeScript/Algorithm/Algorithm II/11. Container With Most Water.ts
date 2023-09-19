function maxArea(height: number[]): number {
  const HEIGHT_LENGTH: number = height.length;

  let maxContainer: number = 0;

  let leftPointer: number = 0;
  let rightPointer: number = HEIGHT_LENGTH - 1;

  while (leftPointer < rightPointer) {
    const leftBar: number = height[leftPointer];
    const rightBar: number = height[rightPointer];
    const barDistance: number = rightPointer - leftPointer;

    const currentContainer: number = Math.min(leftBar, rightBar) * barDistance;
    maxContainer = Math.max(maxContainer, currentContainer);

    if (leftBar < rightBar) leftPointer++;
    else rightPointer--;
  }

  return maxContainer;
}
