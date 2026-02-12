# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None
        saved_data = {}

        while current is not None:
            if current.val in saved_data:
                prev.next = current.next
            else:
                saved_data[current.val] = True
                prev = current
            current = current.next

        return head
        