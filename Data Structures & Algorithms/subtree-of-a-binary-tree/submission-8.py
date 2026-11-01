# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        if (not root) and (not subRoot) or (not subRoot):
            return True

        def finder(node, tar):
            if not node:
                return
            if node.val == tar:
                # if a node is found, then compare the 2 trees
                res_t = helper(node, subRoot)
                if res_t:
                    self.res = True
                    return # early termination
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

        return self.res
'''
if not R or not S:
    return R == S

equals

if ((not R) and S) or (R and (not S)):
    return False
if (not R) and (not S):
    return True

'''
