function mergeTrees(root1: TreeNode | null, root2: TreeNode | null): TreeNode | null {
    if (root1 === null && root2 === null)
        return null;
    
    const rootOneValue: number = root1 ? root1.val : 0;
    const rootTwoValue: number = root2 ? root2.val : 0;

    const mergedTree: TreeNode | null = new TreeNode(rootOneValue + rootTwoValue);
    
    mergedTree.left = mergeTrees(root1 ? root1.left : null, root2 ? root2.left : null);
    mergedTree.right = mergeTrees(root1 ? root1.right : null, root2 ? root2.right : null);

    return mergedTree;
};
