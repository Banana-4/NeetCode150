# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        def pathSum(root, maxSum):
            if not root:
                return -inf                
            l_sum = pathSum(root.left, maxSum)
            r_sum = pathSum(root.right, maxSum)
            path_sum = max(l_sum + root.val, r_sum + root.val, root.val)
            maxSum[0] = max(maxSum[0], l_sum, r_sum, path_sum, l_sum + root.val + r_sum)
            return path_sum
        maxSum = [root.val]
        pathSum(root, maxSum)
        return maxSum[0]
