#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
/** 
 * Definition of a Node
 * struct Node
 * {
 *  int val;
 *  struct Node *right;
 *  struct Node *left;
 *  struct Node *next;
 * };
*/

/*
 * Traverses a binary tree and connects nodes at the same level.
 *
 * The 'traverse' function takes the root node of a binary tree 'root', an array 'previousNode'
 * to track the previous node at each level, the 'level' of the current node, and the 'treeHeight'
 * as input. It recursively traverses the tree and connects nodes at the same level by updating the
 * 'next' pointers. It utilizes a level-order traversal approach.
 *
 * Parameters:
 * - root: The root node of the binary tree.
 * - previousNode: An array to track the previous node at each level.
 * - level: The current level in the tree.
 * - treeHeight: The height of the binary tree.
 */
void traverse(struct Node *root, struct Node **previousNode, int level, int treeHeight)
{
  if (root == NULL)
    return;

  if (previousNode[level])
    previousNode[level]->next = root;

  previousNode[level] = root;
  root->next = NULL;

  traverse(root->left, previousNode, level + 1, treeHeight);
  traverse(root->right, previousNode, level + 1, treeHeight);
}

/*
 * Calculates the height of a binary tree.
 *
 * The 'height' function takes the root node of a binary tree 'root' as input and calculates the
 * height of the binary tree by recursively finding the maximum height of the left and right
 * subtrees and adding 1 to it.
 *
 * Parameters:
 * - root: The root node of the binary tree.
 *
 * Returns:
 * The height of the binary tree.
 */
int height(struct Node *root)
{
  if (root == NULL)
    return 0;

  int leftHeight = height(root->left);
  int rightHeight = height(root->right);

  return (leftHeight > rightHeight) ? (leftHeight + 1) : (rightHeight + 1);
}

/*
 * Connects nodes at the same level in a binary tree.
 *
 * The 'connect' function takes the root node of a binary tree 'root' as input and connects nodes
 * at the same level by calling the 'traverse' function with appropriate arguments. It allocates
 * memory for an array 'previousNode' to track the previous node at each level and then frees
 * the memory before returning the root node.
 *
 * Parameters:
 * - root: The root node of the binary tree.
 *
 * Returns:
 * The root node of the binary tree with 'next' pointers connected.
 */
struct Node *connect(struct Node *root)
{
  int treeHeight = height(root);
  struct Node **previousNode = (struct Node **)malloc(treeHeight * sizeof(struct Node *));
  memset(previousNode, 0, treeHeight * sizeof(struct Node *));

  traverse(root, previousNode, 0, treeHeight);

  free(previousNode);

  return root;
}
