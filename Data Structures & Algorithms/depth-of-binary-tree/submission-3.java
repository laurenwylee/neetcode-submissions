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
    public int maxDepth(TreeNode root) {
        if(root == null)
        {
            return 0;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int count = 0;
        while(!q.isEmpty())
        {
            int sz = q.size();
            count++;
            for(int i = 0; i < sz; i++)
            {
                TreeNode nd = q.remove();
                if(nd.left != null)
                {
                    q.add(nd.left);
                }
                if(nd.right != null)
                {
                    q.add(nd.right);
                }
            }
        }
        return count;
    }
}
