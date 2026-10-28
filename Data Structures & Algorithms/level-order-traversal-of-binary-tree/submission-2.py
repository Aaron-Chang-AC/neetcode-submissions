# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # preorder traversal
        s = [root]
        res = []
        cur = []

        if not root:
            return res

        while s:
            cur = []
            t = []

            for i in s:
                cur.append(i.val)
                if i.left:
                    t.append(i.left)
                if i.right:
                    t.append(i.right)
            
            res.append(cur)
            s = t


            # u=[]
            # for k in s:
            #     u.append(k.val)
            # print(u)
            

        return res