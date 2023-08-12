/* Definition for the max Queue size */
#define MAX_QUEUE_SIZE 10000

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

/*
 * Creates a new queue and returns a pointer to it.
 *
 * The 'createQueue' function allocates memory for a new queue, initializes the
 * front and rear pointers to -1, and returns a pointer to the newly created queue.
 *
 * Returns:
 * A pointer to the newly created queue.
 */
Queue* createQueue() {
    Queue* queue = (Queue*) malloc (sizeof(Queue));
    queue->front = -1;
    queue->rear = -1;
    return queue;
}

/*
 * Checks if a queue is empty.
 *
 * The 'isEmpty' function takes a pointer to a queue 'q' as input and checks whether
 * the queue is empty. It returns 'true' if the front pointer is -1, indicating an
 * empty queue, and 'false' otherwise.
 *
 * Parameters:
 * - q: A pointer to the queue to be checked.
 *
 * Returns:
 * 'true' if the queue is empty, 'false' otherwise.
 */
bool isEmpty(Queue* queue) {
    return queue->front == -1;
}

/*
 * Enqueues a pair into the queue.
 *
 * The 'enqueue' function takes a pointer to a queue 'q' and a pair 'p' as input and
 * enqueues the pair into the queue. It updates the rear pointer and stores the pair
 * data in the data array of the queue.
 *
 * Parameters:
 * - q: A pointer to the queue.
 * - p: The pair to be enqueued.
 */
void enqueue(Queue* queue, Pair pair) {
    if (isEmpty(queue))
        queue->front = queue->rear = 0;
    
    else
        queue->rear++;
    
    queue->data[queue->rear] = pair;
}

/*
 * Dequeues a pair from the queue.
 *
 * The 'dequeue' function takes a pointer to a queue 'q' as input and dequeues a pair
 * from the front of the queue. It retrieves the pair data, updates the front pointer,
 * and returns the dequeued pair.
 *
 * Parameters:
 * - q: A pointer to the queue.
 *
 * Returns:
 * The dequeued pair.
 */
Pair dequeue(Queue* queue) {
    Pair pair = queue->data[queue->front];

    if (queue->front == queue->rear)
        queue->front = queue->rear = -1;
    
    else
        queue->front++;

    return pair;
}

/*
 * Builds the zero distance array for matrix update.
 *
 * The 'buildMatrix' function constructs the zero distance array using a breadth-first
 * search approach. It takes a matrix 'mat', its size 'matSize', column sizes
 * 'matColSize', a zero distance array 'zeroDistanceArray', and pointers to the return
 * size and return column sizes. The function initializes a queue and enqueues all
 * zero elements from 'mat' into the queue. It then performs a breadth-first search
 * by dequeuing pairs from the queue and updating adjacent elements' distances in the
 * zero distance array. The updated zero distance array is constructed after the BFS.
 *
 * Parameters:
 * - mat: The input matrix to be processed.
 * - matSize: The number of rows in the matrix.
 * - matColSize: An array containing the number of columns in each row.
 * - zeroDistanceArray: The zero distance array to be constructed.
 * - returnSize: A pointer to the return size variable.
 * - returnColumnSizes: A pointer to the return column sizes array.
 */
void buildMatrix(int** mat, int matSize, int* matColSize, int** zeroDistanceArray, int* returnSize, int** returnColumnSizes) {
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    *returnSize = matSize;
    *returnColumnSizes = matColSize;
    
    Queue* queue = createQueue();
    
    for (int row = 0; row < matSize; row++) {
        for (int column = 0; column < matColSize[row]; column++) {
            if (mat[row][column] == 0) {
                Pair pair = {row, column};
                enqueue(queue, pair);
            } 
            
            else
                zeroDistanceArray[row][column] = INT_MAX;
        }
    }
    
    while (!isEmpty(queue)) {
        Pair current = dequeue(queue);
        
        for (int k = 0; k < 4; k++) {
            int newRow = current.row + directions[k][0];
            int newCol = current.col + directions[k][1];
            
            if (newRow >= 0 && newRow < matSize && newCol >= 0 && newCol < matColSize[newRow]) {
                if (zeroDistanceArray[current.row][current.col] + 1 < zeroDistanceArray[newRow][newCol]) {
                    zeroDistanceArray[newRow][newCol] = zeroDistanceArray[current.row][current.col] + 1;
                    Pair newPair = {newRow, newCol};
                    enqueue(queue, newPair);
                }
            }
        }
    }
    
    free(queue);
}

/*
 * Updates the zero distance array for matrix with shortest distances to zeros.
 *
 * The 'updateMatrix' function constructs and returns a zero distance array that
 * contains the shortest distances from each cell to the nearest zero element in the
 * input matrix 'mat'. It takes the input matrix 'mat', its size 'matSize', column
 * sizes 'matColSize', a pointer to the return size variable, and a pointer to the
 * return column sizes array. The function allocates memory for the zero distance array,
 * initializes it with zeros, and uses the 'buildMatrix' function to populate the array
 * with the shortest distances to zero elements.
 *
 * Parameters:
 * - mat: The input matrix to be processed.
 * - matSize: The number of rows in the matrix.
 * - matColSize: An array containing the number of columns in each row.
 * - returnSize: A pointer to the return size variable.
 * - returnColumnSizes: A pointer to the return column sizes array.
 *
 * Returns:
 * A pointer to the zero distance array containing the shortest distances to zero
 * elements for each cell in the input matrix.
 */
int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes) {
    int** zeroDistanceArray = (int**) malloc (sizeof(int*) * matSize);
    for (int index = 0; index < matSize; index++)
        zeroDistanceArray[index] = (int*) calloc (sizeof(int), matColSize[index]);
    
    buildMatrix(mat, matSize, matColSize, zeroDistanceArray, returnSize, returnColumnSizes);
    
    return zeroDistanceArray;
}
