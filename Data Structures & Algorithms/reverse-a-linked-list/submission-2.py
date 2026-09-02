# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if not cur:
            return None
        curNext = cur.next 
        cur.next = None
        while cur:
            curNextNext = None
            if curNext:
                curNextNext = curNext.next
                curNext.next = cur
            if not curNext:
                return cur
            cur = curNext
            curNext = curNextNext
        return None 