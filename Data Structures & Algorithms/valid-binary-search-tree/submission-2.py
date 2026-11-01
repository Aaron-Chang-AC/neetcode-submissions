# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def helper(cur, min_v, max_v):
            if (not cur) or (not self.res):
                return
            if cur.val <= min_v or cur.val >= max_v:
                self.res = False
                return

            if cur.left:
                if cur.val > cur.left.val:
                    helper(cur.left, min_v, min(cur.val, max_v)) # set upper limit as current node's
                else:
                    self.res = False
                    return
            if cur.right:
                if cur.val < cur.right.val:
                    helper(cur.right, max(cur.val, min_v), max_v) # upper limit as current node's
                else:
                    self.res = False
                    return
        
        helper(root, -1000000001, 1000000001)
        return self.res
'''
if not cur:
    return

if cur.left:
    if cur.val < cur.left.val:
        self.helper(cur.left, min_v, cur.val) # set upper limit as current node's
    else:
        self.res - False
if cur.right:
    if cur.val > cur.right.val:
        self.helper(cur.right, cur.val, max_v) # upper limit as current node's
    else:
        self.res - False

'''
