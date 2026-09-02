# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sent = ListNode(-1, head)
        # get length of list
        totalLength = 0
        count = head 
        while count:
            totalLength += 1
            count = count.next
        beforeRemoveIndex = totalLength - n

        # find node before the one we want to remove
        index = 0
        curNode = sent
        while index < beforeRemoveIndex:
            curNode = curNode.next
            index += 1

        if curNode.next.next:
            curNode.next = curNode.next.next
        else:
            curNode.next = None

        return sent.next