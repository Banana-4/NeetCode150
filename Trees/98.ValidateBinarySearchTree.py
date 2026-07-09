# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root:Optional[TreeNode] , smallest) -> bool:
            if not root:
                return True
            if not check(root.left, smallest):
                return False
            if smallest and smallest.pop() >= root.val:
                return False
            smallest.append(root.val)
            if not check(root.right, smallest):
                return False
            return True
        return check(root, [])
