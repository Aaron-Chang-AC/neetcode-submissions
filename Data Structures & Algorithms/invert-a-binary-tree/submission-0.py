# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(curr):
            if curr is None:
                return
            if curr.left or curr.right:
                t = curr.right
                curr.right = curr.left
                curr.left = t
            if curr.right:
                rec(curr.right)
            if curr.left:
                rec(curr.left)
            return
        rec(root)
        return root