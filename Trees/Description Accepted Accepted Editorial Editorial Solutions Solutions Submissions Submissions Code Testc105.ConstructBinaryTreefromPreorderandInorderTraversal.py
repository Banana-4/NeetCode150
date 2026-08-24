# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {val: i for i, val in enumerate(inorder)}
        cur = [0]
        def reco(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[cur[0]])
            cur[0] += 1
            root.left = reco(left, indexes[root.val] - 1)
            root.right = reco(indexes[root.val] + 1, right)
            return root
        return reco(0, len(inorder) - 1,)
