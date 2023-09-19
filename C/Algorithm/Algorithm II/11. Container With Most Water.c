#define MIN(X, Y) (X < Y ? X : Y)

#define MAX(X, Y) (X > Y ? X : Y)

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
