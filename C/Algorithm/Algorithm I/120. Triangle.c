#define MIN(X, Y) (X < Y ? X : Y)

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize) {
    for (int row = triangleSize - 2; row > -1; row--) {
        for (int column = 0; column < triangleColSize[row]; column++) {
            int leftOption = triangle[row + 1][column];
            int rightOption = triangle[row + 1][column + 1];
            
            triangle[row][column] += MIN(leftOption, rightOption);
        }
    }

    return triangle[0][0];
}
