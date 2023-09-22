#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

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

int height(struct Node *root)
{
  if (root == NULL)
    return 0;

  int leftHeight = height(root->left);
  int rightHeight = height(root->right);

  return (leftHeight > rightHeight) ? (leftHeight + 1) : (rightHeight + 1);
}

struct Node *connect(struct Node *root)
{
  int treeHeight = height(root);
  struct Node **previousNode = (struct Node **)malloc(treeHeight * sizeof(struct Node *));
  memset(previousNode, 0, treeHeight * sizeof(struct Node *));

  traverse(root, previousNode, 0, treeHeight);

  free(previousNode);

  return root;
}
