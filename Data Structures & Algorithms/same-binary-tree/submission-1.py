# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(P, Q):
            if ((not P) and (Q)) or (not Q) and (P): 
                self.res = False
                return
            if (not P) and (not Q):
                return
            if P.val == Q.val:
                dfs(P.left, Q.left)
                dfs(P.right, Q.right)
            else:
                self.res = False
            return
        
        dfs(p, q)
        return self.res
