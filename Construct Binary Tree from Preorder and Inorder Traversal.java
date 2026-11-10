class Solution {
    private TreeNode build(int lowpre, int highpre,
                           int lowin, int highin,
                           int[] preorder, int[] inorder,
                           HashMap<Integer, Integer> map) {

        if (lowpre > highpre) return null;

        int root = preorder[lowpre];
        TreeNode r = new TreeNode(root);

        int indx = map.get(root);
        int cnt = indx - lowin;

        r.left = build(lowpre + 1, lowpre + cnt,
                       lowin, indx - 1,
                       preorder, inorder, map);

        r.right = build(lowpre + cnt + 1, highpre,
                        indx + 1, highin,
                        preorder, inorder, map);

        return r;
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int n = inorder.length;

        for (int i = 0; i < n; i++) {
            map.put(inorder[i], i);
        }

        return build(0, n - 1, 0, n - 1,
                     preorder, inorder, map);
    }
}
