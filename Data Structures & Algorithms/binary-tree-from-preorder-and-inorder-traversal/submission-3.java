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
    public TreeNode helper(int[] preorder, int pstart, int pend, int[] inorder, int istart, int iend)
    {
        if (pstart == pend) return null;

        TreeNode root = new TreeNode(preorder[pstart]);
        int idx = istart;
        int leftsz = 0;
        while(inorder[idx] != root.val)
        {
            idx++;
            leftsz++;
        }
        root.left = helper(preorder, pstart + 1, pstart + 1 + leftsz, inorder, istart, idx);
        root.right = helper(preorder, pstart + 1 + leftsz, pend, inorder, idx + 1, iend);
        return root;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, 0, preorder.length, inorder, 0, inorder.length);
    }
}
