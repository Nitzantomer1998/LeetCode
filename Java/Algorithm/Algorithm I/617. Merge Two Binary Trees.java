/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

  /**
   * Merges two binary trees by summing the corresponding nodes.
   *
   * @param root1 The root of the first binary tree.
   * @param root2 The root of the second binary tree.
   * @return The merged binary tree.
   */
  public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
    if (root1 == null && root2 == null) return null;

    TreeNode mergedTree = new TreeNode();

    int root1Value = root1 != null ? root1.val : 0;
    int root2Value = root2 != null ? root2.val : 0;

    mergedTree.val = root1Value + root2Value;
    mergedTree.left =
      mergeTrees(
        root1 != null ? root1.left : null,
        root2 != null ? root2.left : null
      );
    mergedTree.right =
      mergeTrees(
        root1 != null ? root1.right : null,
        root2 != null ? root2.right : null
      );

    return mergedTree;
  }
}
