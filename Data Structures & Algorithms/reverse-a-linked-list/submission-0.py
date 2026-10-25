# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        prev = None

        while head is not None:
            res = head
            head = head.next
            res.next = prev
            prev = res
        
        return res
        
