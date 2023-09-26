import java.util.HashMap;
import java.util.Map;

class Solution {

  public int maxPoints(int[][] points) {
    int maxPoints = 0;

    int POINTS_LENGTH = points.length;

    for (int i = 0; i < POINTS_LENGTH; i++) {
      Map<String, Integer> slopeHash = new HashMap<>();

      int maxLocal = 0;

      for (int j = i + 1; j < POINTS_LENGTH; j++) {
        int X1 = points[i][0];
        int Y1 = points[i][1];
        int X2 = points[j][0];
        int Y2 = points[j][1];

        String currentSlope = X1 == X2
          ? "vertical"
          : String.valueOf((double) (Y2 - Y1) / (X2 - X1));
        currentSlope = currentSlope.equals("-0.0") ? "0.0" : currentSlope;

        slopeHash.put(currentSlope, slopeHash.getOrDefault(currentSlope, 0) + 1);

        maxLocal = Math.max(maxLocal, slopeHash.get(currentSlope));
      }

      maxPoints = Math.max(maxPoints, maxLocal + 1);
    }

    return maxPoints;
  }
}
