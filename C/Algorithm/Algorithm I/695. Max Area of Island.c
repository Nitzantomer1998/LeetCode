/* Definition for the max Queue size */
#define MAX_QUEUE_SIZE 2500

/* Definition for getting the maximum value */
#define MAX(X, Y) (X > Y ? X : Y)

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
    queue->front = -1;
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
 * - row: The row index to be enqueued.
 * - col: The column index to be enqueued.
 */
void enqueue(Queue* queue, int row, int col) {
    if (queue->rear == MAX_QUEUE_SIZE - 1)
        return;

    if (queue->front == -1)
        queue->front = 0;

    queue->rear++;
    queue->data[queue->rear].row = row;
    queue->data[queue->rear].col = col;
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
    Pair item;
    item.row = -1;
    item.col = -1;

    if (queue->front == -1 || queue->front > queue->rear)
        return item;

    item = queue->data[queue->front];
    queue->front++;
    return item;
}

/**
 * Checks if the given row and column indices are valid within the grid.
 *
 * The 'isValid' function checks if the provided 'row' and 'col' indices are
 * within valid bounds for the given 'gridSize' and 'gridColSize'.
 *
 * Parameters:
 * - row: The row index to be checked.
 * - col: The column index to be checked.
 * - gridSize: The total number of rows in the grid.
 * - gridColSize: An array containing the number of columns for each row.
 *
 * Returns:
 * '1' if the indices are valid, '0' otherwise.
 */
int isValid(int row, int col, int gridSize, int* gridColSize) {
    return row >= 0 && row < gridSize && col >= 0 && col < gridColSize[row];
}

/**
 * Calculates the maximum area of an island in the given grid.
 *
 * The 'maxAreaOfIsland' function calculates the maximum area of an island in the
 * given 'grid' by performing a breadth-first search (BFS) traversal. It creates a
 * Queue, enqueues the starting cell, and iteratively explores adjacent cells while
 * updating the visited cells. The maximum area of the island is returned.
 *
 * Parameters:
 * - grid: A 2D grid representing land and water.
 * - gridSize: The total number of rows in the grid.
 * - gridColSize: An array containing the number of columns for each row.
 *
 * Returns:
 * The maximum area of an island in the grid.
 */
int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {
    int maxArea = 0;
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    for (int row = 0; row < gridSize; row++) {
        for (int column = 0; column < gridColSize[row]; column++) {
            if (grid[row][column] == 1) {
                int area = 0;
                Queue* queue = createQueue();
                enqueue(queue, row, column);
                
                grid[row][column] = 0;

                while (queue->front <= queue->rear) {
                    Pair current = dequeue(queue);
                    area++;

                    for (int k = 0; k < 4; k++) {
                        int newRow = current.row + directions[k][0];
                        int newCol = current.col + directions[k][1];

                        if (isValid(newRow, newCol, gridSize, gridColSize) && grid[newRow][newCol] == 1) {
                            enqueue(queue, newRow, newCol);
                            grid[newRow][newCol] = 0;
                        }
                    }
                }
                
                maxArea = MAX(maxArea, area);

                free(queue);
            }
        }
    }

    return maxArea;
}
