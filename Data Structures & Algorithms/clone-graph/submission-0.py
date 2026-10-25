
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        res = Node() 
        head = node
        stack = [head]
        addr = {}

        while len(stack) > 0:
            cur = stack.pop(0)
            # print(cur.val)
            # print(stack)
            if cur.val not in addr:
                t2 = Node(cur.val, None)
                addr[cur.val] = t2

            for i in cur.neighbors:
                if i.val not in addr:
                    t3 = Node(i.val, None)
                    addr[i.val] = t3
                    addr[cur.val].neighbors.append(addr[i.val])
                    stack.append(i)
                else:
                    addr[cur.val].neighbors.append(addr[i.val])

        # print(addr)
        return addr.get(1, [])