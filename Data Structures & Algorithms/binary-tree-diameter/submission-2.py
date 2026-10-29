# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            if (not node.left) and (not node.right):
                return 1
            l = dfs(node.left)
            r = dfs(node.right)

            self.res = max(self.res, l + r)
            # print(f"n: {node.val}")
            # print(l)
            # print(r)
            
            return max(l , r) + 1
        
        t = dfs(root)
        return self.res
'''
The thing is for each node we calculate the diameter = max(self.res, l + r)
but we need to return the maximal depth from either left sub-tree or the right sub-tree.
'''
