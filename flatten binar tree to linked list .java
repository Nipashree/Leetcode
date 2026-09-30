class Solution{
private TreeNode prev = null;

public void flatten(TreeNode root) {
    if (root == null) {
        return;
    }

    // Process right subtree first
    flatten(root.right);

    // Then process left subtree
    flatten(root.left);

    // Connect current node to previously processed node
    root.right = prev;
    root.left = null;

    // Update prev
    prev = root;
}
}
