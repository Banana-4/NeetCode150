# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, root, p, q, found, path):
        if not root:
            return False
        if root.val == p:
            found[0] = True
            if not found[1]:
                path.append(root)
            else:
                return True
        if root.val == q:
            found[1] = True
            if not found[0]:
                path.append(root)
            else:
                return True
        if not found[1] and not found[0]:
            path.append(root) 
        if self.DFS( root.left, p, q, found, path) or self.DFS( root.right, p, q, found, path):
            return True
        if root == path[-1]:
            path.pop()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        found = [False, False]
        self.DFS( root, p.val, q.val, found, path)
        return path[-1]
