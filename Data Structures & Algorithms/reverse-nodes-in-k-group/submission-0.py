# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # keep in var head of last group
        # when reaching a new group first traverse group and check if there are at least k elments left
        # go through next full group, reverse, append it to head of last 
        sent = ListNode(next=head)
        last_head = None
        cur = head
        while cur:
            group_counter = 0
            current_head = cur
            # check length:
            while cur and group_counter < k:
                cur = cur.next
                group_counter += 1
            if group_counter < k:
                return sent.next
            cur = current_head
            group_counter = 1
            prev = cur
            cur = cur.next
            while cur and group_counter < k:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                group_counter += 1
            if not last_head:
                sent.next = prev
            else:
                last_head.next = prev
            current_head.next = cur # if remaining nodes form incomplekte group 
            last_head = current_head

        return sent.next
            