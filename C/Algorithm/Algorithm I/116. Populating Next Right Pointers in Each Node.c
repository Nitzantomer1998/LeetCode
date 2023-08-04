void updateNextPointer(struct Node* leftNode, struct Node* rightNode) {
    if (leftNode && rightNode) {
        leftNode->next = rightNode;
        updateNextPointer(leftNode->right, rightNode->left);
    }
}

struct Node* connect(struct Node* root) {
    if (root) {
        updateNextPointer(root->left, root->right);
        connect(root->left);
        connect(root->right);
    }

    return root;
}
