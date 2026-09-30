# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None

        current = temp
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2
        
        
