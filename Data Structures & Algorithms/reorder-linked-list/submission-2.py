# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            if fast:
                slow = slow.next
        right = None
        if slow:
            right = slow.next
            slow.next = None
        def reverseList(head):
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                if next:
                    cur = next
                else:
                    return cur
            return None
        
        def mergeList(l1, l2):
            sent = ListNode(1, None)
            cur = sent
            i = 0
            while l1 and l2:
                if i % 2 == 0:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
                i += 1
            cur.next = l1 if l1 else l2
            return cur
        
        reverseRight = reverseList(right)
        mergeList(head, reverseRight)

                

        