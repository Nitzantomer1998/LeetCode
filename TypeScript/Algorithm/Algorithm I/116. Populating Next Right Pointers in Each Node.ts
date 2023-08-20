function updateNextPointer(leftNode: Node | null, rightNode: Node | null): void {
    if (leftNode && rightNode) {
        leftNode.next = rightNode;
        updateNextPointer(leftNode.right, rightNode.left);
    }
}

function connect(root: Node | null): Node | null {
    if (root) {
        updateNextPointer(root.left, root.right);
        connect(root.left);
        connect(root.right);
    }
    
    return root;
}
