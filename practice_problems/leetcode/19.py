# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # remove nth node from the end of the list and return head

        if head is None:
            return None

        dummy = ListNode(None)
        dummy.next = head
        
        # get length
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        # edge case - need to remove first node
        if length == n:
            dummy.next = dummy.next.next
            return dummy.next
        
        # iterate to one before nth node
        count = length - n - 1
        cur = head

        while cur and count > 0:
            count -= 1
            cur = cur.next
        
        # edge case - need to remove last node
        if cur.next.next is None:
            cur.next = None
        else:
            # remove target node
            cur.next = cur.next.next
        
        return dummy.next