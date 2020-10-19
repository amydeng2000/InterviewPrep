"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        pointer = head
        copy = dummy = Node(0)
        d = {}
        while pointer:
            copy.next = Node(pointer.val)
            copy = copy.next
            d[pointer] = copy
            pointer = pointer.next
        d[pointer] = copy.next
        copy = dummy.next
        pointer = head
        while copy and pointer:
            copy.random = d[pointer.random]
            copy = copy.next
            pointer = pointer.next
        return dummy.next