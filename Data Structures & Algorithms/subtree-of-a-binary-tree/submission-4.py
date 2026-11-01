# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        self.find = []

        if (not root) and (not subRoot) or (not subRoot):
            return True

        def finder(node, tar):
            if not node:
                return
            if node.val == tar:
                self.find.append(node)
            if node.left:
                finder(node.left, tar)
            if node.right:
                finder(node.right, tar)

        def helper(R, S):
            if not R or not S:
                return R == S
            if R.val == S.val:
                return helper(R.left, S.left) and helper(R.right, S.right)
            else:
                return False

        finder(root, subRoot.val)

        if len(self.find) == 0:
            return False

        while self.find:
            r = self.find.pop()
            self.res = helper(r, subRoot)
            if self.res:
                return True
        return False
'''
if not R or not S:
    return R == S

equals

if ((not R) and S) or (R and (not S)):
    return False
if (not R) and (not S):
    return True

'''
