/*
 * Updates the 'next' pointer for a binary tree where each node has an extra 'next'
 * pointer that points to its right node on the same level.
 *
 * The function 'updateNextPointer' is a helper function used to update the 'next'
 * pointers between a left node and its corresponding right node.
 *
 * Parameters:
 * - leftNode: A pointer to the left node.
 * - rightNode: A pointer to the right node.
 *
 * This function recursively updates the 'next' pointers by linking the right node
 * of the left subtree with the left node of the right subtree.
 */
void updateNextPointer(struct Node* leftNode, struct Node* rightNode) {
    if (leftNode && rightNode) {
        leftNode->next = rightNode;
        updateNextPointer(leftNode->right, rightNode->left);
    }
}

/*
 * Connects each node in a binary tree to its adjacent node on the same level
 * using the 'next' pointer.
 *
 * Parameters:
 * - root: A pointer to the root node of the binary tree.
 *
 * Returns:
 * A pointer to the modified root node of the connected binary tree.
 *
 * This function calls the 'updateNextPointer' helper function to update the 'next'
 * pointers between nodes on different levels. It then recursively connects the left
 * and right subtrees of each node.
 */
struct Node* connect(struct Node* root) {
    if (root) {
        updateNextPointer(root->left, root->right);
        connect(root->left);
        connect(root->right);
    }

    return root;
}
