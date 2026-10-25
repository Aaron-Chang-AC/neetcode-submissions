# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur, l):
            self.res = max(self.res, l)
            if cur.left:
                dfs(cur.left, l + 1)
            if cur.right:
                dfs(cur.right, l + 1)
            return
        
        if root is None:
            return 0
        
        dfs(root, 1)
        return self.res