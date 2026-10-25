# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        l = 0
        while t:
            l += 1
            t = t.next
        l = l - n + 1

        if l == 1:
            return head.next

        t = head
        p = None
        while l > 1:
            p = t
            t = t.next
            l -= 1
        p.next = t.next
        return head

'''
[1,2,3,4,5], n = 2

[1 2 3 5]
'''
