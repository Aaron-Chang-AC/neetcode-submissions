# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getlen(self, head: Optional[ListNode]) -> int:
        l = 0
        temp = head
        while temp is not None:
            l+=1
            temp = temp.next
        return l
    def reorderList(self, head: Optional[ListNode]) -> None:
        L = self.getlen(head)

        if L == 1:
            return
        
        mid = L // 2 # The end of the 2nd list (reverse)
        l1 = head
        prev_l2, l2 = None, head

        i = mid
        
        while i > 0:
            l2 = l2.next
            i-=1
        
        t = None
        
        while l2:
            t = l2
            l2 = l2.next
            t.next = prev_l2
            prev_l2 = t
        
        l2 = prev_l2
        i, t = 0, l1
        while i < mid - 1:
            t = t.next
            i+=1
        t.next = None

        res = l1
        prev_l1, t1, t2 = None, None, None

        while l1 and l2:
            t1 = l1
            t2 = l2
            l1 = l1.next
            l2 = l2.next
            t2.next = t1.next
            t1.next = t2
        if l2:
            t2.next=l2
        return





        