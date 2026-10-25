# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        cur1 = list1
        head1 = list1
        prev1 = None

        cur2 = list2

        while cur2:
            cur1 = head1
            prev1 = None
            while cur1:
                if cur2.val <= cur1.val:
                    temp = cur2
                    cur2 = cur2.next
                    temp.next = cur1
                    if prev1 is not None:
                        prev1.next = temp
                    else:
                        head1 = temp
                    break
                elif cur1.next is None:
                    temp = cur2
                    cur1.next = temp
                    cur2 = cur2.next
                    temp.next = None
                    break
                else:
                    prev1 = cur1
                    cur1 = cur1.next
        return head1
            
