# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.p_l=[]
        self.p_find=False
        self.q_l=[]
        self.q_find=False
        def dfs(n, cur, tar, f, res):
            if f or (not n):
                return
            if n.val == tar:
                f = True
                cur.append(n)
                res.extend(cur)
                return 
            cur.append(n)
            if n.left:
                dfs(n.left, cur, tar, f, res)
                cur.pop()
            if n.right:
                dfs(n.right, cur, tar, f, res)
                cur.pop()
        dfs(root, [], p.val, self.p_find, self.p_l)
        dfs(root, [], q.val, self.q_find, self.q_l)
        idx = 0
        # print([i.val for i in self.p_l])
        # print([i.val for i in self.q_l])
        while idx < min(len(self.p_l), len(self.q_l)) and self.p_l[idx].val == self.q_l[idx].val:
            idx+=1
        return self.p_l[idx - 1]
