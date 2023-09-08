/* The isBadVersion API is defined in the parent class VersionControl.
   boolean isBadVersion(int version); */

public class Solution extends VersionControl {

  /**
   * Finds the first bad version in a range of versions using binary search.
   *
   * @param n The highest version number.
   * @return The first bad version found.
   */
  public int firstBadVersion(int n) {
    int leftPointer = 1;
    int rightPointer = n;

    while (leftPointer <= rightPointer) {
      int middlePointer = leftPointer + (rightPointer - leftPointer) / 2;

      if (isBadVersion(middlePointer)) 
        rightPointer = middlePointer - 1;
      
      else 
        leftPointer = middlePointer + 1;
    }

    return rightPointer + 1;
  }
}
