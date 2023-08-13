/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/**
 * Merges two binary trees.
 *
 * The 'mergeTrees' function takes two pointers to binary tree nodes 'root1' and 'root2'
 * as input and merges them into a new binary tree. It creates a new binary tree node for
 * the merged tree, calculates the values of the corresponding nodes in 'root1' and 'root2'
 * (or 0 if a node is missing), and recursively merges the left and right subtrees. The
 * merged tree is constructed by setting the node value and linking the left and right
 * children to the merged subtrees.
 *
 * Parameters:
 * - root1: A pointer to the root node of the first binary tree.
 * - root2: A pointer to the root node of the second binary tree.
 *
 * Returns:
 * A pointer to the root node of the merged binary tree.
 */
struct TreeNode* mergeTrees(struct TreeNode* root1, struct TreeNode* root2) {
    struct TreeNode* mergedTree = (struct TreeNode*) malloc (sizeof(struct TreeNode));

    if (root1 == NULL && root2 == NULL) 
        return NULL;

    int rootOneVal = root1 ? root1->val : 0;
    int rootTwoVal = root2 ? root2->val : 0;

    mergedTree->val = rootOneVal + rootTwoVal;
    mergedTree->left = mergeTrees(root1 ? root1->left : NULL, root2 ? root2->left : NULL);
    mergedTree->right = mergeTrees(root1 ? root1->right : NULL, root2 ? root2->right : NULL);

    return mergedTree;
}
