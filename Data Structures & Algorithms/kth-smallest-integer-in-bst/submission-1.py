# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        s = [root]
        res = []
        while s:
            n = s.pop(0)
            while n:
                s.insert(0, n)
                p = n
                n = n.left
                p.left = None # This is required to avoid infinite loops.
            
            n = s.pop(0)
            res.append(n.val)

            n = n.right
            if n:
                s.insert(0, n)

        return res[k-1]

