"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # map node -> newNode
        nodeMap = {}
        sent = Node(-1, None, None)
        cur1 = head
        cur2 = sent
        while cur1:
            cur2.next = Node(cur1.val, None, None)
            cur2 = cur2.next
            nodeMap[cur1] = cur2
            cur1 = cur1.next
        cur1 = head
        cur2 = sent.next
        while cur1:
            if cur1.random:
                cur2.random = nodeMap[cur1.random]
            else:
                cur2.random = None
            cur1 = cur1.next
            cur2 = cur2.next
        return sent.next


            