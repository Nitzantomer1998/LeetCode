#define MAX_QUEUE_SIZE 2500

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
    queue->front = 0;
    queue->rear = -1;
    return queue;
}

 void enqueue(Queue* queue, Pair pair) {
    queue->rear++;
    queue->data[queue->rear] = pair;
}

 Pair dequeue(Queue* queue) {
    Pair indices = queue->data[queue->front];
    queue->front++;
    return indices;
}

int isValid(int row, int col, int imageSize, int* imageColSize) {
    return row >= 0 && row < imageSize && col >= 0 && col < imageColSize[row];
}

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
