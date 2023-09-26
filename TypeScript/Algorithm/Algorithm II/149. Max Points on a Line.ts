/**
 * Finds the maximum number of points on the same line that can be formed from the given set of points.
 * @param points - A 2D array representing points as [x, y] pairs.
 * @returns The maximum number of points on the same line.
 */
function maxPoints(points: number[][]): number {
  const POINTS_LENGTH: number = points.length;

  let maxPoints: number = 0;

  for (let i: number = 0; i < POINTS_LENGTH; i++) {
    const slopeHash: { [key: string]: number } = {};

    let localMax = 0;

    for (let j: number = i + 1; j < POINTS_LENGTH; j++) {
      const firstPoint: number[] = points[i];
      const secondPoint: number[] = points[j];

      const X1: number = firstPoint[0];
      const Y1: number = firstPoint[1];
      const X2: number = secondPoint[0];
      const Y2: number = secondPoint[1];

      const currentSlope: string =
        X1 === X2 ? "vertical" : ((Y2 - Y1) / (X2 - X1)).toString();

      slopeHash[currentSlope] = (slopeHash[currentSlope] || 0) + 1;

      localMax = Math.max(localMax, slopeHash[currentSlope]);
    }

    maxPoints = Math.max(maxPoints, localMax + 1);
  }

  return maxPoints;
}
