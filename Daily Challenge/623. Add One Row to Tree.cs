public class Solution 
{
    public TreeNode AddOneRow(TreeNode root, int val, int depth) 
    {
        if (depth == 1) return new TreeNode(val, root, null);
        
        Queue<TreeNode> queue = new();
        queue.Enqueue(root);
        
        int currentDepth = 1;
        while (currentDepth < depth - 1)
        {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++)
            {
                TreeNode node = queue.Dequeue();
                
                if (node.left is not null) queue.Enqueue(node.left);
                if (node.right is not null) queue.Enqueue(node.right);
            }
            currentDepth++;
        }
        
        while (queue.Count > 0)
        {
            TreeNode node = queue.Dequeue();
            
            node.left = new TreeNode(val, node.left, null);
            node.right = new TreeNode(val, null, node.right);
        }
        
        return root;
    }
}
