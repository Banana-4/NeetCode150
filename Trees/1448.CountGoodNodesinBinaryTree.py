# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            max_val = max(node.val, max_val)
            return (node.val >= max_val) + good(node.left, max_val) + good(node.right, max_val)
        return good(root, root.val)
