public class Solution 
{
    public int SumOfLeftLeaves(TreeNode root) 
    {
        return DFS(root, false);
    }

    private int DFS(TreeNode node, bool isLeft)
    {
        if (node is null) return 0;
        if (node.left is null && node.right is null && isLeft) return node.val;

        return DFS(node.left, true) + DFS(node.right, false);
    }
}
