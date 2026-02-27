class refInt:
    def __init__(self):
        self.n = 0
class Solution:
    def path(self, root: Optional[TreeNode], diameter: int) -> int:
        left = self.path(root.left, diameter) + 1 if root.left else 0
        right = self.path(root.right, diameter) + 1 if root.right else 0
        diameter.n = max(diameter.n,left, right, left + right)
        return max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = refInt()
        self.path(root, diameter)
        return diameter.n
