# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.append(root)
        s = []
        while q:
            n = q.popleft()
            if n:
                q.append(n.left)
                q.append(n.right)
                s.append(n.val)
            else:
                s.append("null")
        while s and s[-1] == "null":
            s.pop()
        return ",".join(map(str,s))


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None        
  
        d = data.split(',')
        q = deque()
        root  = r = TreeNode(int(d[0]))
        q.append(r)
        c = 2
        for val in  d[1:]:
            if c == 2:
                r  = q.popleft()
                c = 0
            n = None
            if val != "null":
                n = TreeNode(int(val))

            if c == 0:
                r.left = n
            else:
                r.right = n
            c += 1
            if n:
                q.append(n)
     
        return root
           

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
