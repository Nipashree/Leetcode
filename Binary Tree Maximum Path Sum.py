# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # Best contribution we can take from each side.
            # Ignore a side completely if its contribution is negative.
            lmax = max(dfs(node.left), 0)
            rmax = max(dfs(node.right), 0)

            # A complete path can use both sides when this node
            # is the highest point of that path.
            res[0] = max(res[0], node.val + lmax + rmax)

            # The parent can only continue through one branch,
            # so return the better side.
            return node.val + max(lmax, rmax)

        dfs(root)
        return res[0]
