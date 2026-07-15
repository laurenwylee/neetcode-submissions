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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        if(root == null)
        {
            return ret;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        while(!q.isEmpty())
        {
            int sz = q.size();
            for(int i = 0; i < sz - 1; i++)
            {
                TreeNode nd = q.remove();
                if(nd.left != null) {q.add(nd.left);}
                if(nd.right != null) {q.add(nd.right);}
            }
            TreeNode nd = q.remove();
            if(nd.left != null) {q.add(nd.left);}
            if(nd.right != null) {q.add(nd.right);}
            ret.add(nd.val);
        }
        return ret;
    }
}
