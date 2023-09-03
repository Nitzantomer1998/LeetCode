/**
 * Definition for a binary tree node.
 * @class TreeNode
 * @property {number} val - The value of the node.
 * @property {TreeNode | null} left - The left child node.
 * @property {TreeNode | null} right - The right child node.
 * @constructor Create a TreeNode.
 * @param {number} [val] - The value of the node.
 * @param {TreeNode | null} [left] - The left child node.
 * @param {TreeNode | null} [right] - The right child node.
 *
 * class TreeNode {
 *     val: number;
 *     left: TreeNode | null;
 *     right: TreeNode | null;
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val === undefined ? 0 : val);
 *         this.left = (left === undefined ? null : left);
 *         this.right = (right === undefined ? null : right);
 *     }
 * }
 */

/**
 * Merges two binary trees by summing their node values.
 * @param {TreeNode | null} root1 - The root node of the first tree.
 * @param {TreeNode | null} root2 - The root node of the second tree.
 * @returns {TreeNode | null} The root node of the merged binary tree.
 */
function mergeTrees(root1: TreeNode | null, root2: TreeNode | null): TreeNode | null {
  if (root1 === null && root2 === null) return null;

  const rootOneValue: number = root1 ? root1.val : 0;
  const rootTwoValue: number = root2 ? root2.val : 0;

  const mergedTree: TreeNode | null = new TreeNode(rootOneValue + rootTwoValue);

  mergedTree.left = mergeTrees(root1 ? root1.left : null, root2 ? root2.left : null);
  mergedTree.right = mergeTrees(root1 ? root1.right : null, root2 ? root2.right : null);

  return mergedTree;
}
