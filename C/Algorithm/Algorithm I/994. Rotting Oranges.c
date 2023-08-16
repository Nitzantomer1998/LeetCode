/* Definitions of the max queue size */
#define MAX_QUEUE_SIZE 100

/* Definitions for the values of the orange */
#define EMPTY 0
#define FRESH 1
#define ROTTEN 2


typedef struct {
    int array[MAX_QUEUE_SIZE];
    int front;
    int rear;
    int size;
} Queue;

/**
 * Enqueues an item into the given queue.
 *
 * The 'enqueue' function adds an 'item' to the rear of the queue 'queue'.
 * If the queue is already at maximum capacity, the function does nothing.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 * - item: The item to be enqueued.
 */
void enqueue(Queue* queue, int item) {
    if (queue->size == MAX_QUEUE_SIZE)
        return;
    
    queue->rear = (queue->rear + 1) % MAX_QUEUE_SIZE;
    queue->array[queue->rear] = item;
    queue->size++;
}

/**
 * Dequeues an item from the given queue.
 *
 * The 'dequeue' function removes and returns an item from the front of the queue 'queue'.
 * If the queue is empty, the function returns '-1'.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 *
 * Returns:
 * The item at the front of the queue, or '-1' if the queue is empty.
 */
int dequeue(Queue* queue) {
    if (isEmpty(queue))
        return -1;

    int item = queue->array[queue->front];
    queue->front = (queue->front + 1) % MAX_QUEUE_SIZE;
    queue->size--;
    
    return item;
}

/**
 * Checks if the given queue is empty.
 *
 * The 'isEmpty' function determines whether the queue 'queue' is empty.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 *
 * Returns:
 * '1' if the queue is empty, '0' otherwise.
 */
int isEmpty(Queue* queue) {
    return queue->size == 0;
}

/**
 * Initializes a queue.
 *
 * The 'createQueue' function initializes the queue 'queue' by setting its front and size to zero,
 * and its rear to the maximum capacity minus one.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 */
void createQueue(Queue* queue) {
    queue->front = queue->size = 0;
    queue->rear = MAX_QUEUE_SIZE - 1;
}

/**
 * Checks if the given row and column indices are valid within the grid.
 *
 * The 'isValid' function checks if the provided 'row' and 'col' indices are
 * within valid bounds for a grid of size 'rows' x 'columns'.
 *
 * Parameters:
 * - rows: The total number of rows in the grid.
 * - columns: The total number of columns in the grid.
 * - row: The row index to be checked.
 * - col: The column index to be checked.
 *
 * Returns:
 * '1' if the indices are valid, '0' otherwise.
 */
int isValid(int rows, int columns, int row, int column) {
    return row >= 0 && row < rows && column >= 0 && column < columns;
}

/**
 * Calculates the minimum time for all oranges to become rotten.
 *
 * The 'orangesRotting' function calculates the minimum time required for all
 * fresh oranges in the grid to become rotten. It uses a breadth-first search
 * approach starting from initially rotten oranges.
 *
 * Parameters:
 * - grid: A 2D grid representing the orange status.
 * - gridSize: The total number of rows in the grid.
 * - gridColSize: An array containing the number of columns for each row.
 *
 * Returns:
 * The minimum time for all fresh oranges to become rotten, or '-1' if not all oranges can be rotten.
 */
int orangesRotting(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = *gridColSize;
    
    Queue queue;
    createQueue(&queue);

    for (int row = 0; row < rows; row++)
        for (int column = 0; column < cols; column++)
            if (grid[row][column] == ROTTEN)
                enqueue(&queue, row * cols + column);

    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int minutesCounter = 0;

    while (!isEmpty(&queue)) {
        int size = queue.size;

        for (int i = 0; i < size; i++) {
            int cell = dequeue(&queue);
            int row = cell / cols;
            int col = cell % cols;
            
            for (int d = 0; d < 4; d++) {
                int newRow = row + directions[d][0];
                int newCol = col + directions[d][1];

                if (isValid(rows, cols, newRow, newCol) && grid[newRow][newCol] == FRESH) {
                    grid[newRow][newCol] = ROTTEN;
                    enqueue(&queue, newRow * cols + newCol);
                }
            }
        }
        
        if (!isEmpty(&queue))
            minutesCounter++;
    }

    for (int row = 0; row < rows; row++)
        for (int column = 0; column < cols; column++)
            if (grid[row][column] == FRESH)
                return -1;

    return minutesCounter;
}
