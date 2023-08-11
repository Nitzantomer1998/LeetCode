#define MAX_QUEUE_SIZE 10000

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
    Queue* q = (Queue*) malloc (sizeof(Queue));
    q->front = -1;
    q->rear = -1;
    return q;
}

bool isEmpty(Queue* q) {
    return q->front == -1;
}

void enqueue(Queue* q, Pair p) {
    if (isEmpty(q))
        q->front = q->rear = 0;
    
    else
        q->rear++;
    
    q->data[q->rear] = p;
}

Pair dequeue(Queue* q) {
    Pair p = q->data[q->front];

    if (q->front == q->rear)
        q->front = q->rear = -1;
    
    else
        q->front++;

    return p;
}

void buildMatrix(int** mat, int matSize, int* matColSize, int** zeroDistanceArray, int* returnSize, int** returnColumnSizes) {
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    *returnSize = matSize;
    *returnColumnSizes = matColSize;
    
    Queue* q = createQueue();
    
    for (int row = 0; row < matSize; row++) {
        for (int column = 0; column < matColSize[row]; column++) {
            if (mat[row][column] == 0) {
                Pair p = {row, column};
                enqueue(q, p);
            } 
            
            else
                zeroDistanceArray[row][column] = INT_MAX;
        }
    }
    
    while (!isEmpty(q)) {
        Pair current = dequeue(q);
        
        for (int k = 0; k < 4; k++) {
            int newRow = current.row + directions[k][0];
            int newCol = current.col + directions[k][1];
            
            if (newRow >= 0 && newRow < matSize && newCol >= 0 && newCol < matColSize[newRow]) {
                if (zeroDistanceArray[current.row][current.col] + 1 < zeroDistanceArray[newRow][newCol]) {
                    zeroDistanceArray[newRow][newCol] = zeroDistanceArray[current.row][current.col] + 1;
                    Pair p = {newRow, newCol};
                    enqueue(q, p);
                }
            }
        }
    }
    
    free(q);
}

int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes) {
    int** zeroDistanceArray = (int**) malloc (sizeof(int*) * matSize);
    for (int index = 0; index < matSize; index++)
        zeroDistanceArray[index] = (int*) calloc (matColSize[index], sizeof(int));
    
    buildMatrix(mat, matSize, matColSize, zeroDistanceArray, returnSize, returnColumnSizes);
    
    return zeroDistanceArray;
}
