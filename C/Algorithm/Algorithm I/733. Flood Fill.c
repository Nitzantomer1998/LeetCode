/* Definition for the max Queue size */
#define MAX_QUEUE_SIZE 2500

/* A structure to represent a pair of integers (row, col). */
typedef struct {
    int row;
    int col;
} Pair;

/* A structure to represent a queue of pairs. */
typedef struct {
    Pair data[MAX_QUEUE_SIZE];
    int front;
    int rear;
} Queue;

/**
 * Creates a new Queue and returns a pointer to it.
 *
 * The 'createQueue' function dynamically allocates memory for a new Queue,
 * initializes its front and rear indices, and returns a pointer to the
 * newly created Queue.
 *
 * Returns:
 * A pointer to the newly created Queue.
 */
 Queue* createQueue() {
    Queue* queue = (Queue*) malloc (sizeof(Queue));
    queue->front = 0;
    queue->rear = -1;
    return queue;
}

/**
 * Enqueues a Pair into the given Queue.
 *
 * The 'enqueue' function adds a Pair with specified 'row' and 'col' values
 * to the rear of the Queue, updating the rear index. If the Queue is full,
 * the function does not enqueue any new element.
 *
 * Parameters:
 * - queue: A pointer to the Queue.
 * - pair: The row and column index to be enqueued.
 */
 void enqueue(Queue* queue, Pair pair) {
    queue->rear++;
    queue->data[queue->rear] = pair;
}

/**
 * Dequeues and returns a Pair from the given Queue.
 *
 * The 'dequeue' function removes and returns the Pair at the front of the Queue,
 * updating the front index. If the Queue is empty or the front index exceeds
 * the rear index, a special Pair with (-1, -1) values is returned.
 *
 * Parameters:
 * - queue: A pointer to the Queue.
 *
 * Returns:
 * The Pair at the front of the Queue, or a special Pair (-1, -1) if the Queue is empty.
 */
 Pair dequeue(Queue* queue) {
    Pair indices = queue->data[queue->front];
    queue->front++;
    return indices;
}

/**
 * Checks if the given row and column indices are valid within the image.
 *
 * The 'isValid' function checks if the provided 'row' and 'col' indices are
 * within valid bounds for the given 'imageSize' and 'imageColSize'.
 *
 * Parameters:
 * - row: The row index to be checked.
 * - col: The column index to be checked.
 * - imageSize: The total number of rows in the image.
 * - imageColSize: An array containing the number of columns for each row.
 *
 * Returns:
 * '1' if the indices are valid, '0' otherwise.
 */
int isValid(int row, int col, int imageSize, int* imageColSize) {
    return row >= 0 && row < imageSize && col >= 0 && col < imageColSize[row];
}

/**
 * Flood-fill the given image starting from the specified position.
 *
 * The 'floodFill' function fills the connected region of the image with the specified 'color'
 * starting from the position ('sr', 'sc'). It uses a breadth-first search approach with a queue
 * to process adjacent pixels. The function modifies the input 'image' and returns the updated image.
 *
 * Parameters:
 * - image: A 2D array representing the image to be modified.
 * - imageSize: The total number of rows in the image.
 * - imageColSize: An array containing the number of columns for each row.
 * - sr: The starting row index for flood-fill.
 * - sc: The starting column index for flood-fill.
 * - color: The new color to be filled in the region.
 * - returnSize: A pointer to the variable that will store the number of rows in the modified image.
 * - returnColumnSizes: An array to store the number of columns for each row in the modified image.
 *
 * Returns:
 * A modified 2D array representing the image after flood-fill.
 */
int** floodFill(int** image, int imageSize, int* imageColSize, int sr, int sc, int color, int* returnSize, int** returnColumnSizes) {
    int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int originalColor = image[sr][sc];

    if (originalColor == color) {
        *returnSize = imageSize;
        *returnColumnSizes = imageColSize;
        return image;
    }

    Queue* queue = createQueue();
    enqueue(queue, (Pair){sr, sc});

    while (queue->front <= queue->rear) {
        Pair current = dequeue(queue);
        int row = current.row;
        int col = current.col;

        image[row][col] = color;

        for (int i = 0; i < 4; i++) {
            int newRow = row + directions[i][0];
            int newCol = col + directions[i][1];

            if (isValid(newRow, newCol, imageSize, imageColSize) && image[newRow][newCol] == originalColor) {
                enqueue(queue, (Pair){newRow, newCol});
                image[newRow][newCol] = color;
            }
        }
    }

    free(queue);

    *returnSize = imageSize;
    *returnColumnSizes = imageColSize;

    return image;
}
