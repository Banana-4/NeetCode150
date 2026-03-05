class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = depth(root.left)
            if left == -1:
                return -1
            right = depth(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        return  depth(root) != -1
