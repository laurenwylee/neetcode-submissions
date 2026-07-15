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

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String ret = "";
        Queue<TreeNode> q = new LinkedList<>();
        if(root == null)
        {
            return ret;
        }
        q.add(root);
        int layer = 0;
        while(!q.isEmpty())
        {
            TreeNode nd = q.remove();
            if(nd != null)
            {
                ret = ret + nd.val + ",";
                q.add(nd.left);
                q.add(nd.right);
            } else
            {
                ret += "N,";
            }
        }
        System.out.print(ret);
        return ret;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "")
        {
            return null;
        }
        String[] vals = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        int i = 1;
        while(!q.isEmpty() && i < vals.length)
        {
            TreeNode nd = q.remove();
            if (!vals[i].equals("N"))
            {
                nd.left = new TreeNode(Integer.parseInt(vals[i]));
                q.add(nd.left);
            }
            i += 1;
            if(!vals[i].equals("N"))
            {
                nd.right = new TreeNode(Integer.parseInt(vals[i]));
                q.add(nd.right);
            }
            i += 1;
        }
        return root;
    }
}
