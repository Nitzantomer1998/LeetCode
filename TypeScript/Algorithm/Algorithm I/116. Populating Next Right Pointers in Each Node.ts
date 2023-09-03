/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     left: Node | null
 *     right: Node | null
 *     next: Node | null
 *     constructor(val?: number, left?: Node, right?: Node, next?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 * Updates the 'next' pointers of nodes in a binary tree according to specific rules.
 * @param {Node | null} leftNode - The left node.
 * @param {Node | null} rightNode - The right node.
 */
function updateNextPointer(leftNode: Node | null, rightNode: Node | null): void {
  if (leftNode && rightNode) {
    leftNode.next = rightNode;
    updateNextPointer(leftNode.right, rightNode.left);
  }
}

/**
 * Connects nodes in a binary tree to their adjacent nodes in the same level.
 * @param {Node | null} root - The root node of the binary tree.
 * @returns {Node | null} The root node of the modified binary tree.
 */
function connect(root: Node | null): Node | null {
  if (root) {
    updateNextPointer(root.left, root.right);
    connect(root.left);
    connect(root.right);
  }

  return root;
}
