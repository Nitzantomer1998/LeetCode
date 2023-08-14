#define MAX_QUEUE_SIZE 2500

#define MAX(X, Y) (X > Y ? X : Y)

typedef struct {
    int row;
    int col;
} Pair;

typedef struct {
    Pair data[MAX_QUEUE_SIZE];
    int front;
    int rear;
} Queue;

Queue* createQueue() {
    Queue* queue = (Queue*) malloc (sizeof(Queue));
    queue->front = -1;
    queue->rear = -1;
    return queue;
}

void enqueue(Queue* queue, int row, int col) {
    if (queue->rear == MAX_QUEUE_SIZE - 1)
        return;

    if (queue->front == -1)
        queue->front = 0;

    queue->rear++;
    queue->data[queue->rear].row = row;
    queue->data[queue->rear].col = col;
}

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

int isValid(int row, int col, int gridSize, int* gridColSize) {
    return row >= 0 && row < gridSize && col >= 0 && col < gridColSize[row];
}

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
