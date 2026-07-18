class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            res = inorder(root.left)
            if res > -1:
                return res
            self.k -= 1
            if self.k == 0:
                return root.val
            res = inorder(root.right)
            return res
        self.k = k
        return inorder(root)
