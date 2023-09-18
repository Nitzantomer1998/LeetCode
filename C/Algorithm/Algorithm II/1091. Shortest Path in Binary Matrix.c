#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* A structure to represent a node (row, column, distance). */
typedef struct Node
{
    int row;
    int column;
    int distance;
    struct Node *next;
} Node;

/* A structure to represent a queue of nodes. */
typedef struct
{
    Node *front;
    Node *rear;
} Queue;

/*
 * Creates a new queue and returns a pointer to it.
 *
 * The 'createQueue' function allocates memory for a new queue, initializes the front
 * and rear pointers to NULL, and returns a pointer to the newly created queue.
 *
 * Returns:
 * A pointer to the newly created queue.
 */
Queue *createQueue()
{
    Queue *queue = (Queue *)malloc(sizeof(Queue));

    queue->front = NULL;
    queue->rear = NULL;

    return queue;
}

/*
 * Checks if a queue is empty.
 *
 * The 'isEmpty' function takes a pointer to a queue 'queue' as input and checks whether
 * the queue is empty. It returns 'true' if the front pointer is NULL, indicating an
 * empty queue, and 'false' otherwise.
 *
 * Parameters:
 * - queue: A pointer to the queue to be checked.
 *
 * Returns:
 * 'true' if the queue is empty, 'false' otherwise.
 */
bool isEmpty(Queue *queue) { return queue->front == NULL; }

/*
 * Enqueues a new element with specified row, column, and distance into the queue.
 *
 * The 'enqueue' function takes a pointer to a queue 'queue', along with row, column, and
 * distance values, and adds a new node with these values to the rear of the queue. It
 * dynamically allocates memory for the new node.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 * - row: The row value to enqueue.
 * - column: The column value to enqueue.
 * - distance: The distance value to enqueue.
 */
void enqueue(Queue *queue, int row, int column, int distance)
{
    Node *newNode = (Node *)malloc(sizeof(Node));

    newNode->row = row;
    newNode->column = column;
    newNode->distance = distance;
    newNode->next = NULL;

    if (isEmpty(queue))
    {
        queue->front = newNode;
        queue->rear = newNode;
    }

    else
    {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
}

/*
 * Dequeues an element from the queue.
 *
 * The 'dequeue' function takes a pointer to a queue 'queue' as input and removes and returns
 * the front element from the queue. It also updates the front pointer of the queue.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 *
 * Returns:
 * A pointer to the dequeued node.
 */
Node *dequeue(Queue *queue)
{
    Node *frontNode = queue->front;

    queue->front = queue->front->next;

    if (queue->front == NULL)
        queue->rear = NULL;

    return frontNode;
}

/*
 * Calculates the size of the queue.
 *
 * The 'queueSize' function takes a pointer to a queue 'queue' as input and calculates the
 * current size of the queue (number of elements in the queue) by traversing the linked list
 * of nodes.
 *
 * Parameters:
 * - queue: A pointer to the queue.
 *
 * Returns:
 * The size of the queue.
 */
int queueSize(Queue *queue)
{
    int size = 0;
    Node *currentNode = queue->front;

    while (currentNode != NULL)
    {
        size++;
        currentNode = currentNode->next;
    }

    return size;
}

/*
 * Frees the memory allocated for the queue and its nodes.
 *
 * The 'freeQueue' function takes a pointer to a queue 'queue' as input and frees the memory
 * allocated for the queue and all its nodes. It ensures that there are no memory leaks.
 *
 * Parameters:
 * - queue: A pointer to the queue to be freed.
 */
void freeQueue(Queue *queue)
{
    while (!isEmpty(queue))
    {
        Node *frontNode = dequeue(queue);
        free(frontNode);
    }
    free(queue);
}

/*
 * Checks if a given cell is a valid cell in the grid.
 *
 * The 'isValidCell' function takes row, column, total rows (ROWS), and total columns (COLUMNS)
 * as input and checks if the cell specified by the row and column values is a valid cell within
 * the grid boundaries.
 *
 * Parameters:
 * - row: The row index of the cell.
 * - column: The column index of the cell.
 * - ROWS: The total number of rows in the grid.
 * - COLUMNS: The total number of columns in the grid.
 *
 * Returns:
 * True if the cell is valid; otherwise, returns False.
 */
bool isValidCell(int row, int column, int ROWS, int COLUMNS)
{
    int isValidRow = row >= 0 && row < ROWS;
    int isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
}

/*
 * Finds the shortest path in a binary matrix using BFS.
 *
 * The 'shortestPathBinaryMatrix' function takes a binary matrix 'grid', its grid size 'gridSize',
 * and the array 'gridColSize' representing the number of columns. It uses a breadth-first search
 * (BFS) approach to find the shortest path from the top-left corner to the bottom-right corner of
 * the matrix. If a valid path exists, it returns the length of the shortest path; otherwise, it
 * returns -1.
 *
 * Parameters:
 * - grid: The binary matrix representing obstacles (0) and open cells (1).
 * - gridSize: The number of rows in the grid.
 * - gridColSize: The number of columns in each row of the grid.
 *
 * Returns:
 * The length of the shortest path or -1 if no path exists.
 */
int shortestPathBinaryMatrix(int **grid, int gridSize, int *gridColSize)
{
    int ROWS = gridSize;
    int COLUMNS = gridColSize[0];

    int directions[8][2] = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1},
        {-1, -1},
        {-1, 1},
        {1, -1},
        {1, 1},
    };

    Queue *queue = createQueue();

    if (grid[0][0] == 0)
    {
        enqueue(queue, 0, 0, 1);
        grid[0][0] = 1;
    }

    while (!isEmpty(queue))
    {
        int currentLevel = queueSize(queue);

        for (int level = 0; level < currentLevel; level++)
        {
            Node *frontNode = dequeue(queue);

            int currentRow = frontNode->row;
            int currentCol = frontNode->column;
            int currentDistance = frontNode->distance;

            free(frontNode);

            if (currentRow == ROWS - 1 && currentCol == COLUMNS - 1)
                return currentDistance;

            for (int direction = 0; direction < 8; direction++)
            {
                int newRow = currentRow + directions[direction][0];
                int newCol = currentCol + directions[direction][1];

                if (isValidCell(newRow, newCol, ROWS, COLUMNS) && grid[newRow][newCol] == 0)
                {
                    enqueue(queue, newRow, newCol, currentDistance + 1);
                    grid[newRow][newCol] = 1;
                }
            }
        }
    }

    freeQueue(queue);

    return -1;
}
