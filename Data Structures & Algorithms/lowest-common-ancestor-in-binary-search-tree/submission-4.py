# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res=None
        def dfs(n, p, q):
            if n.val < p.val and n.val < q.val:
                dfs(n.right, p, q)
            elif n.val > p.val and n.val > q.val:
                dfs(n.left, p, q)
            else:
                self.res=n
        dfs(root, p, q)
        return self.res

'''
LCA is the first node that splits p and q.
'''