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
