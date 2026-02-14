# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        prev1 = dummy1
        prev2 = dummy2
        current = head

        while current:
            next_node = current.next
            current.next = None
            if current.val < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next            
            current = next_node

        prev1.next = dummy2.next
        return dummy1.next
        