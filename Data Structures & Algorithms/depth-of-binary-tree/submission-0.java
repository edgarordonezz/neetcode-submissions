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
        if (root == null) return 0;

        // traverse the left subtree
        int leftDepth = maxDepth(root.left);
        // traverse the right subtree
        int rightDepth = maxDepth(root.right);

        // return max depth subtree + 1 to account for current node
        return Math.max(leftDepth, rightDepth) + 1;


    }
}
