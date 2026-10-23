class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self._left_most_inorder(root)

    def _left_most_inorder(self, root: TreeNode | None):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top_node = self.stack.pop()
        if top_node.right:
            self._left_most_inorder(top_node.right)
            
        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
