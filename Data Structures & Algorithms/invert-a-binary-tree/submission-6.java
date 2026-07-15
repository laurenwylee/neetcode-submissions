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
    public TreeNode invertTree(TreeNode root) {
        if(root == null)
        {
            return root;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        while(!q.isEmpty())
        {
            TreeNode nd = q.poll();
            TreeNode left = nd.left;
            nd.left = nd.right;
            nd.right = left;

            if(nd.right != null)
            {
                q.add(nd.right);
            }
            if(nd.left != null)
            {
                q.add(nd.left);
            }
        }
        return root;
    }
}
