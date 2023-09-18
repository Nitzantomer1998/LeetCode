#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node
{
    int row;
    int column;
    int distance;
    struct Node *next;
} Node;

typedef struct
{
    Node *front;
    Node *rear;
} Queue;

Queue *createQueue()
{
    Queue *queue = (Queue *)malloc(sizeof(Queue));

    queue->front = NULL;
    queue->rear = NULL;

    return queue;
}

bool isEmpty(Queue *queue) { return queue->front == NULL; }

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

Node *dequeue(Queue *queue)
{
    Node *frontNode = queue->front;

    queue->front = queue->front->next;

    if (queue->front == NULL)
        queue->rear = NULL;

    return frontNode;
}

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

void freeQueue(Queue *queue)
{
    while (!isEmpty(queue))
    {
        Node *frontNode = dequeue(queue);
        free(frontNode);
    }
    free(queue);
}

bool isValidCell(int row, int column, int ROWS, int COLUMNS)
{
    int isValidRow = row >= 0 && row < ROWS;
    int isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
}

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
