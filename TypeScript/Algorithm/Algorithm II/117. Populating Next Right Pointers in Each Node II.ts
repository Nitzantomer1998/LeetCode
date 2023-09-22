/* Definition for Node
 * class Node {
 *   val: number;
 *   left: Node | null;
 *   right: Node | null;
 *   next: Node | null;
 *   constructor(val?: number, left?: Node, right?: Node, next?: Node) {
 *     this.val = val === undefined ? 0 : val;
 *     this.left = left === undefined ? null : left;
 *     this.right = right === undefined ? null : right;
 *     this.next = next === undefined ? null : next;
 *   }
 * }
*/

/**
 * Connects each node in a binary tree to its adjacent node in the same level,
 * using the "next" pointer.
 *
 * @param root - The root node of the binary tree.
 * @returns The root node of the modified binary tree with "next" pointers set.
 */
function connect(root: Node | null): Node | null {
  const queue: Node[] = [root!];

  while (queue && queue[0]) {
    const currentLevel: number = queue.length;

    for (let level: number = 0; level < currentLevel; level++) {
      let currentNode: Node = queue.shift()!;

      if (level < currentLevel - 1)
        currentNode.next = queue[0];

      if (currentNode.left) 
        queue.push(currentNode.left);

      if (currentNode.right) 
        queue.push(currentNode.right);
    }
  }

  return root;
}
