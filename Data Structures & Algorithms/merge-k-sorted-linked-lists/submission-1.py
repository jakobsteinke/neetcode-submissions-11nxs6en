# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(-1, None)
        cur = sent
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        return sent.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1:
            return lists[0]
        length = len(lists)
        merge1 = self.mergeKLists(lists[:length//2])
        merge2 = self.mergeKLists(lists[length//2:])
        return self.mergeTwoLists(merge1, merge2)

        