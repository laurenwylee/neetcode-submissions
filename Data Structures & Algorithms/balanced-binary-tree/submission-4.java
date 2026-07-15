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
    public int[] height(TreeNode root)
    {
        if(root == null)
        {
            return new int[]{0, 1};
        }

        int[] left = height(root.left);
        int[] right = height(root.right);

        int balanced;
        if(Math.abs(left[0] - right[0]) <= 1 && left[1] == 1 && right[1] == 1 )
        {
            balanced = 1;
        } else
        {
            balanced = 0;
        }

        return new int[]{1 + Math.max(left[0], right[0]), balanced};
    }
    public boolean isBalanced(TreeNode root) {
       if(height(root)[1] == 1)
       {
            return true;
       } else
       {
            return false;
       }
    }
}
