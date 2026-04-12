# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        cur = head
        while cur:
            len += 1
            cur = cur.next
        delI = len - n + 1
        count = 1
        cur = head
        bef = None
        while count != delI:
            bef = cur
            cur = cur.next
            count += 1
        if bef:
            bef.next = cur.next
        if cur is head and len == 1:
            return None
        if cur is head:
            return head.next
        return head 