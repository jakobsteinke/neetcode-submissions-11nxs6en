# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sent = ListNode(1, None)
        prev = sent
        while l1 and l2:
            sum = l1.val + l2.val + carry
            overflow = sum - (sum % 10)
            prev.next = ListNode(sum % 10, None)
            if overflow != 0:
                carry = 1
            else: 
                carry = 0
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            overflow = sum - (sum % 10)
            prev.next = ListNode(sum % 10, None)
            if overflow != 0:
                carry = 1
            else: 
                carry = 0
            prev = prev.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            overflow = sum - (sum % 10)
            prev.next = ListNode(sum % 10, None)
            if overflow != 0:
                carry = 1
            else: 
                carry = 0
            prev = prev.next
            l2 = l2.next
        if carry:
            prev.next = ListNode(1, None)
        return sent.next
