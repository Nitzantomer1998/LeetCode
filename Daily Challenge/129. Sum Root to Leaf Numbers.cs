public class Solution
{
    public int SumNumbers(TreeNode root)
    {
        return DFS(root, 0);
    }

    private int DFS(TreeNode node, int currentSum)
    {
        if (node is null) return 0;

        int newSum = currentSum * 10 + node.val;

        if (node.left is null && node.right is null) return newSum;
        return DFS(node.left, newSum) + DFS(node.right, newSum);
    }
}
