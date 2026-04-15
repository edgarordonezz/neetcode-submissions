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
        Queue<TreeNode> q = new LinkedList<>();
        if (root != null) {
            q.add(root);
        }

        int level = 0;
        // while q isnt empty
        while (!q.isEmpty()) {
            int size = q.size();
            // traverse size of tree
            for (int i = 0; i < size; i++) {
                // get node sitting in queue
                TreeNode node = q.poll();
                // if node sitting in queue is not null add
                if (node.left != null) {
                    q.add(node.left);
                }
                // check independently
                if (node.right != null) {
                    q.add(node.right);
                }
            }
            // add to level
            level++;
        }
        return level;
    }
}
