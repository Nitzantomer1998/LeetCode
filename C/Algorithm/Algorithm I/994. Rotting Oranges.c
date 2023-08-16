#define MAX_QUEUE_SIZE 100

#define EMPTY 0
#define FRESH 1
#define ROTTEN 2


typedef struct {
    int array[MAX_QUEUE_SIZE];
    int front;
    int rear;
    int size;
} Queue;

void enqueue(Queue* queue, int item) {
    if (queue->size == MAX_QUEUE_SIZE)
        return;
    
    queue->rear = (queue->rear + 1) % MAX_QUEUE_SIZE;
    queue->array[queue->rear] = item;
    queue->size++;
}

int dequeue(Queue* queue) {
    if (isEmpty(queue))
        return -1;

    int item = queue->array[queue->front];
    queue->front = (queue->front + 1) % MAX_QUEUE_SIZE;
    queue->size--;
    
    return item;
}

int isEmpty(Queue* queue) {
    return queue->size == 0;
}

void createQueue(Queue* queue) {
    queue->front = queue->size = 0;
    queue->rear = MAX_QUEUE_SIZE - 1;
}

int isValid(int rows, int columns, int row, int column) {
    return row >= 0 && row < rows && column >= 0 && column < columns;
}

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
