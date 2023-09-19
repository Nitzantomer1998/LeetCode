/* Definition for getting the minimum value */
#define MIN(X, Y) (X < Y ? X : Y)

/* Definition for getting the maximum value */
#define MAX(X, Y) (X > Y ? X : Y)

/*
 * Calculates the maximum area between vertical bars.
 *
 * The 'maxArea' function takes an array 'height' representing the heights of vertical bars
 * and its size 'heightSize' as input. It calculates the maximum area between two vertical bars
 * by using a two-pointer approach. The function iterates through the array while adjusting the
 * pointers to maximize the area between the bars. The result is the maximum area that can be
 * enclosed by two bars.
 *
 * Parameters:
 * - height: An array representing the heights of vertical bars.
 * - heightSize: The number of elements in the 'height' array.
 *
 * Returns:
 * The maximum area between two vertical bars.
 */
int maxArea(int *height, int heightSize)
{
    int HEIGHT_LENGTH = heightSize;
    int maxContainer = 0;
    int leftPointer = 0;
    int rightPointer = HEIGHT_LENGTH - 1;

    while (leftPointer < rightPointer)
    {
        int leftBar = height[leftPointer];
        int rightBar = height[rightPointer];
        int barDistance = rightPointer - leftPointer;

        int currentContainer = MIN(leftBar, rightBar) * barDistance;
        maxContainer = MAX(maxContainer, currentContainer);

        if (leftBar < rightBar)
            leftPointer++;

        else
            rightPointer--;
    }

    return maxContainer;
}
